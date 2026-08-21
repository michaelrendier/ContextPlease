#!/bin/bash
# NVMe transplant repair: HP EliteBook 820 G3 -> Lenovo ThinkPad X1 Carbon 6th gen
# 2026-08-19.  Run as root via pkexec.
#
# Fixes, in order of what actually broke:
#   1. vboxdrv.sh livelock  (MOK key absent from new motherboard NVRAM ->
#      infinite Secure Boot password prompt with no tty -> journal flood)
#   2. phantom systemd units for hardware this machine does not have
#   3. 142 stale kernel packages making every apt upgrade a 4-hour event
#
# Does NOT touch: /home, lighttpd, hostname, the MOK enrollment itself.

set -o pipefail

D=/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-08-19_nvme-transplant-repair
LOG="$D/repair.log"
exec > >(tee -a "$LOG") 2>&1

echo "===== repair started $(date -Is) ====="
echo "kernel: $(uname -r)   host: $(hostname)"
echo

echo "--- [1/6] masking vboxdrv"
echo "    (prevents the MOK prompt livelock recurring on the next boot;"
echo "     unmask after the MOK is enrolled or Secure Boot is disabled)"
systemctl mask vboxdrv.service && echo "    masked vboxdrv.service"
echo

echo "--- [2/6] masking phantom units (no such hardware on this machine)"
for u in casper-md5check.service pd-mapper.service rmtfs.service qcom-modem-setup.service; do
  systemctl mask "$u" >/dev/null 2>&1 && echo "    masked $u"
done
echo

echo "--- [3/6] creating missing adbusers group (silences udev rule spam)"
if getent group adbusers >/dev/null; then
  echo "    adbusers already exists"
else
  groupadd adbusers && echo "    created adbusers"
fi
usermod -aG adbusers rendier && echo "    added rendier to adbusers"
echo

echo "--- [4/6] purging old kernel packages"
echo "    keeping: 6.8.0-138-lowlatency (running), 6.8.0-138-generic, 6.8.0-137-lowlatency"
COUNT=$(wc -l < "$D/purge-candidates.txt")
echo "    purging: $COUNT packages"
DEBIAN_FRONTEND=noninteractive apt-get -y purge $(tr '\n' ' ' < "$D/purge-candidates.txt")
echo "    purge exit: $?"
echo

echo "--- [5/6] regenerating initramfs for all remaining kernels"
update-initramfs -u -k all
echo "    initramfs exit: $?"
echo

echo "--- [6/6] updating grub"
update-grub
echo "    grub exit: $?"
echo

echo "===== repair finished $(date -Is) ====="
echo
echo "--- disk after:"
df -h / /boot/efi
echo
echo "--- kernels remaining:"
ls -1 /boot/vmlinuz-*
echo
echo "--- failed units after:"
systemctl --failed --no-pager
