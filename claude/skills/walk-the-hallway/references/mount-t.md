# mount(8) — the parts the hallway depends on

Source: `man mount` on this machine, util-linux 2.39.3 (libmount 2.39.3), read 2026-10-17.
Excerpts are verbatim from that manual page (util-linux, GPL-2.0-or-later); everything after "NOTES" is mine.

## -t, --types fstype  (verbatim)

    The argument following the -t is used to indicate the filesystem type. The filesystem types
    which are currently supported depend on the running kernel. See /proc/filesystems and
    /lib/modules/$(uname -r)/kernel/fs for a complete list of the filesystems. The most common
    are ext2, ext3, ext4, xfs, btrfs, vfat, sysfs, proc, nfs and cifs.

    If no -t option is given, or if the auto type is specified, mount will try to guess the
    desired type. mount uses the libblkid(3) library for guessing the filesystem type; if that
    does not turn up anything that looks familiar, mount will try to read the file
    /etc/filesystems, or, if that does not exist, /proc/filesystems. All of the filesystem types
    listed there will be tried, except for those that are labeled "nodev" (e.g. devpts, proc and
    nfs). ... While trying, all filesystem types will be mounted with the mount option silent.

    More than one type may be specified in a comma-separated list, for the -t option as well as
    in an /etc/fstab entry. The list of filesystem types for the -t option can be prefixed with
    no to specify the filesystem types on which no action should be taken. The prefix no has no
    effect when specified in an /etc/fstab entry.

        mount -a -t nomsdos,smbfs     # mounts all filesystems except those of type msdos and smbfs

    The programs mount and umount(8) support filesystem subtypes. The subtype is defined by a
    '.subtype' suffix. For example 'fuse.sshfs'.

## Same file, several filesystems at once  (verbatim)

    The same filesystem may be mounted more than once ... The mount command does not implement
    any policy to control this behavior. All behavior is controlled by the kernel and it is
    usually specific to the filesystem driver.

## LOOP-DEVICE SUPPORT  (verbatim)

    mount /tmp/disk.img /mnt -t vfat -o loop=/dev/loop3
    mount /tmp/disk.img /mnt -o loop
    The mount command automatically creates a loop device from a regular file if a filesystem
    type is not specified or the filesystem is known for libblkid ...
    Since Linux 2.6.25 auto-destruction of loop devices is supported, meaning that any loop device
    allocated by mount will be freed by umount ...
    Since util-linux v2.29, mount re-uses the loop device rather than initializing a new device
    if the same backing file is already used for some loop device with the same offset and
    sizelimit. This is necessary to avoid a filesystem corruption.

## Non-superuser mounts  (verbatim, shortened)

    Normally, only the superuser can mount filesystems. However, when fstab contains the user
    option on a line, anybody can mount the corresponding filesystem.

## NOTES (mine, measured or derived)

1. The comma list is an ORDERED probe: the first type that mounts wins. `-t ext4,vfat,exfat` is
   "try ext4, then vfat, then exfat". Put likelier types first.
2. The manual itself excludes `nodev` lines from probing. A `nodev` type has no block device
   behind it (proc, sysfs, tmpfs, cgroup, securityfs, debugfs, ...): the SOURCE ARGUMENT IS
   IGNORED and the mount shows a kernel view, not the file. So "mount the file as type X" for a
   nodev X cannot show what is inside the file.
3. `-o ro,nosuid,nodev,noexec` on every probe. Never write to the image.
4. Unprivileged route: fstab `user` entries (above), or userspace drivers (fuse2fs, squashfuse,
   ntfs-3g, libguestfs). WalkTheHalls.py (Phaleron) uses libguestfs for that reason.
5. `findmnt -n -o TARGET,FSTYPE,SOURCE <mountpoint>` confirms a probe really mounted; trust it
   over the exit code of a wrapper script.
