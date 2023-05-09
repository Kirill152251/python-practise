# Write an algorithm that will identify valid IPv4
# addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets,
# with values between 0 and 255, inclusive.
# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4 / 123.45.67.89
# Invalid input examples:
# 1.2.3 / 1.2.3.4.5 / 123.456.78.90 / 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string
def is_valid_ip(str_ip: str):
    octets = str_ip.split('.')
    if len(octets) != 4:
        return False
    for part in octets:
        if not part.isdigit():
            return False
        if part.startswith('0') and len(part) > 1:
            return False
        int_octet = int(part)
        if 0 <= int_octet <= 255:
            continue
        else:
            return False
    return True


print(is_valid_ip("123.456.789.0"))
