from ssh_lib.config import ASSETS_DIR
from ssh_lib.utils import apt_get_install, apt_get_purge, put, put_str


def setup_kernel_settings(c):
    put(c, f'{ASSETS_DIR}/kernel/60-ofm.conf', '/etc/sysctl.d/')
    put(c, f'{ASSETS_DIR}/kernel/limits-ofm.conf', '/etc/security/limits.d/')


def set_cpu_governor(c):
    apt_get_install(c, 'cpufrequtils')
    apt_get_purge(c, 'linux-tools-*')

    put_str(
        c,
        '/etc/default/cpufrequtils',
        'GOVERNOR="performance"',
    )

    # check after reboot
    # cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
