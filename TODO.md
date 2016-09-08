To do:
- Single, and double, quotation marks look funny, in the terminal,
  when they're pickled and I think that this is because of the
  sloppy `sed` command that I ran to replace the single
  quotation marks with the double quotation marks. This would
  probably be a good time to review the "stop words" and
  see if there are any other "stop words" that should be added
  to ignore.py--especially jargon that is related to finance.

- The front-end could look better.

- It'd be nice to write this to Postgres, but that was such
  a pain in the ass, last time; I'd rather focus on doubling
  down on sentiment analysis so Katabasis can generate
  original data from audio (utterance_transcriber); video
  (frame_grabber); images (ie. frames)(object_tracer); and
  text (ie. documents)(screen_scrapers).

- Jenna mentioned CockroachDB. Sounds disgusting, but they could
  be onto something. They're backed by Google Ventures (they're
  ex-Googlers) and Sequoia Capital. Jenna said that she's friends
  with the founder and that she's been trying to get him to speak
  at Byte, for some time, now. After all, cockroaches are resilient.
  And: I hate Postgres.

- Now: sentiment analysis
