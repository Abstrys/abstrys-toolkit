# SRep Recipes

## Removing Oxygen comments

If you work with developers who use Oxygen, you might find your source files littered with `<?oxy_insert_start>`,
`<?oxy_insert_end>`, and `<?oxy_option>` tags. These can even appear in the midst of text, screwing up the flow of your
topics.

To remove these, use the following `srep` command:

    srep '<\?oxy.*?>' '' *.xml

