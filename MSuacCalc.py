import sys


# https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/useraccountcontrol-manipulate-account-properties#list-of-property-flags
USER_ACCOUNT_CONTROL = {
    "SCRIPT": 0x0001,
    "ACCOUNTDISABLE": 0x0002,
    "HOMEDIR_REQUIRED": 0x0008,
    "LOCKOUT": 0x0010,
    "PASSWD_NOTREQD": 0x0020,
    "PASSWD_CANT_CHANGE": 0x0040,
    "ENCRYPTED_TEXT_PASSWORD_ALLOWED": 0x0080,
    "TEMP_DUPLICATE_ACCOUNT": 0x0100,
    "NORMAL_ACCOUNT": 0x0200,
    "INTERDOMAIN_TRUST_ACCOUNT": 0x0800,
    "WORKSTATION_TRUST_ACCOUNT": 0x1000,
    "SERVER_TRUST_ACCOUNT": 0x2000,
    "DONT_EXPIRE_PASSWORD": 0x10000,
    "MNS_LOGON_ACCOUNT": 0x20000,
    "SMARTCARD_REQUIRED": 0x40000,
    "TRUSTED_FOR_DELEGATION": 0x80000,
    "NOT_DELEGATED": 0x100000,
    "USE_DES_KEY_ONLY": 0x200000,
    "DONT_REQ_PREAUTH": 0x400000,
    "PASSWORD_EXPIRED": 0x800000,
    "TRUSTED_TO_AUTH_FOR_DELEGATION": 0x1000000,
    "NO_AUTH_DATA_REQUIRED": 0x02000000,
    "PARTIAL_SECRETS_ACCOUNT": 0x04000000
}


if len(sys.argv) != 2:
    print("Usage: python ms-uac_calc.py <UserAccountControl value>")
else:
    input_value = sys.argv[1]
    binary_value = int(input_value, 10)

    attributes = []

    for attribute, bitmask in USER_ACCOUNT_CONTROL.items():
        if binary_value & bitmask:
            attributes.append(attribute)

    print("UserAccountControl Value:", input_value)
    print("Corresponding Attributes:", ", ".join(attributes))
