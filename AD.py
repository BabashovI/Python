import ldap

LDAP_SERVER_EMG = "ldaps://10.qwe.0.2"
BIND_DN = "qwe.qw@qwe.com"
BIND_PASS = "qwe"
USER_BASE = "dc=emgS,dc=local"
try:
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 0)
    lcon_emg = ldap.initialize(LDAP_SERVER_EMG)
    lcon_emg.simple_bind_s(BIND_DN, BIND_PASS)
except ldap.LDAPError as e:
    print(e)
