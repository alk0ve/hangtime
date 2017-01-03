import os
import argparse


HANGTIME_EXE_NAME = "HANGTIME.EXE"
HANGTIME_EXE_SIZE = 1188352

FIRST_PATCH_OFFSET = 0x1051C2
FIRST_EXPECTED_CONTENTS = 'USER32.dll'
FIRST_NEW_CONTENTS = 'USSR32.dll'

SECOND_PATCH_OFFSET = 0xAE1AC
SECOND_EXPECTED_CONTENTS = 'user32.dll'
SECOND_NEW_CONTENTS = 'ussr32.dll'


PATCHED_EXE_NAME = "HANGTIME_USSR.EXE"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hangtime_exe_path",
                        help="Location of HANGTIME.EXE (default is the working directory)",
                        default=HANGTIME_EXE_NAME,
                        nargs='?')
    args = parser.parse_args()

    if not os.path.isfile(args.hangtime_exe_path):
        print "ERROR: either provide a path to HANGTIME.EXE or run the script from the same directory"
        return

    with open(args.hangtime_exe_path, 'rb') as f:
        content = bytearray(f.read())

    assert (len(content) == HANGTIME_EXE_SIZE and
            content[FIRST_PATCH_OFFSET: FIRST_PATCH_OFFSET + len(FIRST_EXPECTED_CONTENTS)] == FIRST_EXPECTED_CONTENTS
            and content[SECOND_PATCH_OFFSET: SECOND_PATCH_OFFSET + len(SECOND_EXPECTED_CONTENTS)]
            == SECOND_EXPECTED_CONTENTS), \
        "Wrong executable size (wrong version?)"

    content[FIRST_PATCH_OFFSET: FIRST_PATCH_OFFSET + len(FIRST_EXPECTED_CONTENTS)] = FIRST_NEW_CONTENTS
    content[SECOND_PATCH_OFFSET: SECOND_PATCH_OFFSET + len(SECOND_EXPECTED_CONTENTS)] = SECOND_NEW_CONTENTS

    with open(os.path.join(os.path.dirname(args.hangtime_exe_path), PATCHED_EXE_NAME), 'wb') as f:
        f.write(content)


if __name__ == "__main__":
    main()
