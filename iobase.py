"""Example of context manager usage."""


import os
import sys
import time


def test1(file_name="test1.txt",
          delay=0,
          line_length=100,
          exc_count=-1,
          exit_count=-1,
          abort_count=-1,
          max_count=500) -> None:
    """_summary_.

    Args:
        file_name: Nazwa wyjściowego pliku. Defaults to "test1.txt".
        delay: Opóźnienie pomiędzy zapisem kolejnego znaku do pliku
               wyjściowego. Umożliwia przerwanie testu za pomocą np. Ctrl-C.
               Defaults to 0.
        line_length: Długość linii zapisywanej do pliku. Określa jak często
                     wykonywana jest operacja flush na pliku wyjściowym.
                     Defaults to 100.
        exc_count: Numer znaku po którym wyrzucany jest wyjątek AssertionError.
                   Defaults to -1.
        exit_count: Numer znaku po którym wołana jest funkcja sys.exit().
                    Defaults to -1.
        abort_count: Numer znaku po którym wołana jest funkcja os.abort().
                     Defaults to -1.
        max_count: Maksymalna ilość znakó pisanych do pliku wyjściowego.
                   Defaults to 500.
    """
    try:
        with open(file_name, "w", encoding="utf8") as file:
            for count in range(1, max_count + 1):

                # Print character to a file
                print("*", end="", file=file)

                # Show progress on a console
                print(count, end="\r")

                # Conditional delay between characters to enable Ctrl-C
                if delay > 0:
                    time.sleep(delay)  # Ctrl-C during execution causes
                    # KeyboardInterrupt and works OK, but this exception
                    # is not caught by our try/except.

                # Generate AssertionError exception
                if count == exc_count:
                    assert False  # Works OK

                # Exit from an appplication with sys.exit()
                if count == exit_count:
                    sys.exit()  # Works OK

                # Exit from an appplication with os.abort()
                if count == abort_count:
                    os.abort()  # Does not flush buffers

                # End line in output file to force flush
                if count > 0 and count % line_length == 0:
                    print(file=file)
    except Exception as exc:
        print(type(exc))

    # Show output file size to show if everything was flushed.
    stat = os.stat(file_name)
    print(F"File_size: {stat.st_size} bytes")


if __name__ == "__main__":
    # Run test generation various situation during writing to a file.
    test1(file_name="test1.txt",
          delay=0,
          line_length=100,
          exc_count=-1,
          exit_count=-1,
          abort_count=-1)
