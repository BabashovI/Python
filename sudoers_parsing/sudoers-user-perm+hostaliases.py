import datetime
import os
import glob
import re


def get_sudoers_files(env):
    hdir = os.environ["HOME"]
    if env == '1':
        sudoers = f"{hdir}/qwe"
        sudoers_tmpl = f"{hdir}qwe/sudoers.d"
        sudoers_dir = f"{hdir}qwe/sudoers.d"
        sudoers_files = [sudoers] + glob.glob(os.path.join(
            sudoers_tmpl, '*')) + glob.glob(os.path.join(
                sudoers_dir, '*'))
    elif env == '2':
        sudoers = f"{hdir}/qwe/sudoers"
        sudoers_dir = f"{hdir}/qwe/sudoers.d"
        sudoers_files = [sudoers] + glob.glob(os.path.join(
            sudoers_dir, '*'))
    return sudoers_files


def extract_aliases_and_rules(sudoers_files):
    Host_Aliases = []
    Cmnd_Aliases = []
    User_Aliases = []
    Rules = []
    for filename in sudoers_files:
        with open(filename, 'r') as su:
            for line in su:
                if '#' not in line:
                    if 'Host_Alias' in line:
                        Host_Aliases.append(line.strip())
                    elif 'Cmnd_Alias' in line:
                        Cmnd_Aliases.append(line.strip())
                    elif 'User_Alias' in line:
                        User_Aliases.append(line.strip())
                    elif '=(' in line:
                        Rules.append(line.strip())
    return Host_Aliases, Cmnd_Aliases, User_Aliases, Rules


def get_rules_for_group(group, Rules):
    pattern = r'^\w*{}\w*\b'
    return [r.strip() for r in Rules if re.match(pattern.format(group), r, flags=re.I | re.X)]


def get_group_user_info(group, User_Aliases):
    pattern = r'\w*{}\w*\b'
    for g_u in User_Aliases:
        if re.match(pattern.format(group), g_u, flags=re.I | re.X):
            print(g_u)


def print_related_host_aliases(rule, Host_Aliases):
    for r in rule.split()[1].split("=")[0].split(','):
        for host in Host_Aliases:
            if f"Host_Alias {r.lstrip(' !')}" == host.split("=")[0].rstrip():
                print("  ", host)
                for sub_h in host.split("="):
                    for sub_hh in sub_h.split(","):
                        if "Host_Alias" not in sub_hh:
                            for host in Host_Aliases:
                                if f"Host_Alias {sub_hh.lstrip(' !')}" ==\
                                        host.split("=")[0].rstrip():
                                    print("    ", host)
                                    for sub_hhh in host.split('='):
                                        if "Host_Alias" not in sub_hhh:
                                            for sub_hhhh in sub_hhh.split(','):
                                                for host in Host_Aliases:
                                                    if f"Host_Alias {sub_hhhh.lstrip(' !')}" ==\
                                                            host.split("=")[0].rstrip():
                                                        print(
                                                            "      ", host)


env = input("Enter 1(OCI) or 2(Classic): ")
group = input("Enter group alias: ")

Host_Aliases, Cmnd_Aliases, User_Aliases, Rules = extract_aliases_and_rules(
    get_sudoers_files(env))
rule_results = get_rules_for_group(group, Rules)
# print(User_Aliases)
get_group_user_info(group, User_Aliases)

start_time = datetime.datetime.now()
for rule in rule_results:
    print("+------------------------------------------------------+")
    print(rule)
    print_related_host_aliases(rule, Host_Aliases)
print("+------------------------------------------------------+")
end_time = datetime.datetime.now()
print(end_time - start_time)
