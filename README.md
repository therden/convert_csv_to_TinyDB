# Converting CSV files to TinyDB files

This repo contains a sample csv file and two short programs demonstrating its conversion into a **TinyDB** file.

They were written to respond to [this question](https://github.com/msiemens/tinydb/discussions/380) in the _Discussions_ section of [Marcus Siemens' TinyDB repo on Github](https://github.com/msiemens/tinydb).

By default, **TinyDB** generates and associates a sequential numeric `doc_id` to each record inserted into its database. As suggested by their filenames, one program uses that default behavior, while the other assigns the `id` field in the source file to the `doc_id` field of the **TinyDB** record.
