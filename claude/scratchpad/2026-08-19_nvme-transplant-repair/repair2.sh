#!/bin/bash
# NVMe transplant repair -- PART 2 (steps 4-6)
# Steps 1-3 (mask vboxdrv, mask phantom units, adbusers group) already
# succeeded in the first run; see repair.log.
#
# Fixes the bug in repair.sh: the purge failed soft with exit 100 (dpkg
# lock held by mintUpdate) and the script marched on into the expensive
# initramfs step anyway. This version ABORTS if the purge does not succeed.

D=/home/rendier/Projects/ThePlace/.claude/scratchpad/2026-08-19_nvme-transplant-repair
LOG="$D/repair.log"
exec > >(tee -a "$LOG") 2>&1

echo
echo "===== repair PART 2 started $(date -Is) ====="

echo "--- [0/3] pre-flight: dpkg lock must be free"
if fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1; then
  echo "!!! ABORT: dpkg lock is held. Close Update Manager and retry."
  exit 1
fi
echo "    lock is free"
echo

echo "--- [0b/3] clearing interrupted-run leftovers"
rm -fv /boot/initrd.img-*.new
echo

echo "--- [1/3] purging old kernel packages"
COUNT=$(wc -l < "$D/purge-candidates.txt")
echo "    keeping: 6.8.0-138-lowlatency (running), 6.8.0-138-generic, 6.8.0-137-lowlatency"
echo "    purging: $COUNT packages"
DEBIAN_FRONTEND=noninteractive apt-get -y purge $(tr '\n' ' ' < "$D/purge-candidates.txt")
RC=$?
if [ $RC -ne 0 ]; then
  echo "!!! ABORT: purge failed with exit $RC -- NOT proceeding to initramfs."
  echo "!!! (this is the guard that was missing from repair.sh)"
  exit $RC
fi
echo "    purge OK"
echo "    kernels now in /boot: $(ls -1 /boot/vmlinuz-* 2>/dev/null | wc -l)"
echo

echo "--- [2/3] regenerating initramfs for remaining kernels"
update-initramfs -u -k all
echo "    initramfs exit: $?"
echo

echo "--- [3/3] updating grub"
update-grub
echo "    grub exit: $?"
echo

echo "===== repair PART 2 finished $(date -Is) ====="
echo
echo "--- disk after:"
df -h / /boot/efi
echo
echo "--- kernels remaining:"
ls -1 /boot/vmlinuz-*
echo
echo "--- failed units:"
systemctl --failed --no-pager
echo
echo "--- DKMS status:"
dkms status
