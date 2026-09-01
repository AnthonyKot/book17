One TSV per chapter, `NN.tsv`, tab-separated, five columns:

    chapter	claim id	one-line claim as made in prose	source (URL or citation with page/section)	status

Status is `checked-by:<who>:<YYYY-MM-DD>` or `open`. Claim ids are `NN-` prefixed and
match `<!-- CHECK: id -->` markers in the chapter HTML one to one. Lines starting with
`#` are comments.
