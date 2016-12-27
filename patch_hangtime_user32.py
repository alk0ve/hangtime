import os
import argparse


HANGTIME_EXE_NAME = "HANGTIME.EXE"
HANGTIME_EXE_SIZE = 1188352
PATCH_OFFSET = 0x1051c2
EXPECTED_CONTENTS = 'USER32.dll'
NEW_CONTENTS = 'USSR32.dll'
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
            content[PATCH_OFFSET: PATCH_OFFSET + len(EXPECTED_CONTENTS)] == EXPECTED_CONTENTS), \
        "Wrong executable size (wrong version?)"

    content[PATCH_OFFSET: PATCH_OFFSET + len(EXPECTED_CONTENTS)] = NEW_CONTENTS

    with open(os.path.join(os.path.dirname(args.hangtime_exe_path), PATCHED_EXE_NAME), 'wb') as f:
        f.write(content)


if __name__ == "__main__":
    main()
