## Overview

This code produces the dataset at https://huggingface.co/datasets/gardner/nz_legislation

The resulting data is in `jsonl` format and each line contains:

```json
{
    "id": "DLM415522",
    "year": "1974",
    "title": "Ngarimu VC and 28th (Maori) Battalion Memorial Scholarship Fund Amendment Act 1974",
    "text": "1: Short Title\nThis Act may be cited as the Ngarimu VC and 28th (Maori) Battalion Memorial Scholarship Fund Amendment Act 1974, and shall be read together with and deemed part of the Ngarimu VC and 28th (Maori) Battalion Memorial Scholarship Fund Act 1945\n2:\n3:\n4: New sections substituted\n1: This subsection substituted section 14 section 15\n2: Notwithstanding anything in subsection (1) subsection (1)\n3: Notwithstanding anything in section 15 subsection (1)"
}
```

## Copyright

The legislation text data in this dataset repository has **no copyright**.

From the Legislation.govt.nz [website](https://legislation.govt.nz/about.aspx#copyright):

> There is no copyright in New Zealand Acts, Bills, or the secondary legislation published on this website (see [section 27 of the Copyright Act 1994](https://legislation.govt.nz/act/public/1994/0143/latest/DLM345939.html)). All Acts, Bills, Supplementary Order Papers, and secondary legislation published on this website may be reproduced free of charge in any format or media without requiring specific permission.

## Challenges

A few challenges in producing this dataset mainly arose due to standards support by the publisher. Specifically:

* The character sets differ from document to document.
* The HTTP server does not support Last-Modified headers.
* The XML files contain innacurate metadata.
