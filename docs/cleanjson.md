# cleanjson.md

Usage: cleanjson.py [inputfile] [outputfile]

If *inputfile* is not provided, input will be read from **stdin** and delivered to **stdout**.

If *outputfile* is not provided, output will be delivered to **stdout**.

**Note:** You cannot set *outputfile* unless *inputfile* was also set.

## Examples

**Clean json from input.json and write to output.json:**

    cleanjson.py input.json output.json

**Clean json from stdin and write to stdout:**

   cleanjson.py <input.json

**Clean json from stdin and write to stdout (file):**

   cleanjson.py <input.json >output.json

**You can also use cleanjson.py as a pipe:**

   cat input.json | cleanjson.py >output.json

