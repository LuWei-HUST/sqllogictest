hash-threshold 8

statement ok
CREATE TABLE tab0(col0 INT, col1 INT, col2 INT)

statement ok
CREATE TABLE tab1(col0 INT, col1 INT, col2 INT)

statement ok
CREATE TABLE tab2(col0 INT, col1 INT, col2 INT)

statement ok
INSERT INTO tab0 VALUES(89,91,82)

statement ok
INSERT INTO tab0 VALUES(35,97,1)

statement ok
INSERT INTO tab0 VALUES(24,86,33)

statement ok
INSERT INTO tab1 VALUES(64,10,57)

statement ok
INSERT INTO tab1 VALUES(3,26,54)

statement ok
INSERT INTO tab1 VALUES(80,13,96)

statement ok
INSERT INTO tab2 VALUES(7,31,27)

statement ok
INSERT INTO tab2 VALUES(79,17,38)

statement ok
INSERT INTO tab2 VALUES(78,59,26)

query IIIIII rowsort
SELECT distinct * FROM tab2, tab2 cor0
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query IIIIII rowsort
SELECT * FROM tab1, tab2 cor0
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query IIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query III rowsort
SELECT distinct * FROM tab1 AS cor0
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query III rowsort
SELECT * FROM tab0 AS cor0
----
9 values hashing to 38a1673e2e09d694c8cec45c797034a7

query IIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query III rowsort
SELECT distinct * FROM tab2
----
9 values hashing to ad05b5942400d5e7a21b323b3da65a45

query III rowsort
SELECT * FROM tab2
----
9 values hashing to ad05b5942400d5e7a21b323b3da65a45

query III rowsort
SELECT distinct * FROM tab0
----
9 values hashing to 38a1673e2e09d694c8cec45c797034a7

query III rowsort
SELECT distinct * FROM tab1
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab1 cor0
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query III rowsort
SELECT * FROM tab0 cor0
----
9 values hashing to 38a1673e2e09d694c8cec45c797034a7

query III rowsort
SELECT * FROM tab2 AS cor0
----
9 values hashing to ad05b5942400d5e7a21b323b3da65a45

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab0 AS cor0, tab0 AS cor1
----
243 values hashing to 3e8bd9634a3f5947d8becd5f5799bb7f

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab1 AS cor0
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query III rowsort
SELECT * FROM tab0
----
9 values hashing to 38a1673e2e09d694c8cec45c797034a7

query IIIIII rowsort
SELECT distinct * FROM tab2, tab2 AS cor0
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query I rowsort
SELECT distinct col0 AS col1 FROM tab2 AS cor0
----
7
78
79

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 AS cor0, tab0 AS cor1
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query III rowsort
SELECT * FROM tab1 AS cor0
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query I rowsort
SELECT distinct cor0.col0 * 59 FROM tab0, tab1 AS cor0
----
177
3776
4720

query III rowsort
SELECT distinct * FROM tab2 AS cor0
----
9 values hashing to ad05b5942400d5e7a21b323b3da65a45

query IIIIII rowsort
SELECT distinct * FROM tab0, tab1 cor0
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query I rowsort
SELECT tab1.col1 + 77 AS col0 FROM tab1, tab0 AS cor0
----
9 values hashing to e95026a3b232313ec2d8a183f7b1cc4c

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab1 AS cor1
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1, tab1 AS cor0
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query III rowsort
SELECT distinct * FROM tab2 cor0
----
9 values hashing to ad05b5942400d5e7a21b323b3da65a45

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab2 AS cor0
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query IIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1, tab0 AS cor0
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query IIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query IIIIII rowsort
SELECT distinct * FROM tab0, tab1 AS cor0
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query III rowsort
SELECT distinct * FROM tab0 AS cor0
----
9 values hashing to 38a1673e2e09d694c8cec45c797034a7

query I rowsort
SELECT cor0.col1 + - 13 FROM tab2 AS cor0
----
18
4
46

query I rowsort
SELECT ALL + 78 * col1 AS col2 FROM tab1
----
1014
2028
780

query IIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab1 AS cor1
----
243 values hashing to 2464a6f4cfabe66aeca50fcb4cd85bf5

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 cor0, tab0 AS cor1
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query III rowsort
SELECT * FROM tab1
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query IIIIII rowsort
SELECT distinct * FROM tab0, tab0 AS cor0
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab0 AS cor1
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query I rowsort
SELECT col1 * tab0.col1 FROM tab0
----
7396
8281
9409

query I rowsort
SELECT col0 * col2 * col2 FROM tab2
----
114076
5103
52728

query I rowsort
SELECT distinct - - col1 FROM tab0 AS cor0
----
86
91
97

query IIIIII rowsort
SELECT distinct * FROM tab2, tab0 cor0
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query I rowsort
SELECT ALL + - col2 * - cor0.col1 AS col1 FROM tab1 AS cor0
----
1248
1404
570

query I rowsort
SELECT ALL - - cor0.col1 + 25 FROM tab0 AS cor0
----
111
116
122

query I rowsort
SELECT - col1 + cor0.col1 FROM tab2 AS cor0
----
0
0
0

query I rowsort
SELECT distinct - - 57 FROM tab0 AS cor0
----
57

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0, tab0 AS cor1
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query I rowsort
SELECT ALL + col1 AS col0 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT distinct col0 * 9 + - col2 AS col2 FROM tab0 AS cor0
----
183
314
719

query I rowsort
SELECT ALL + 28 AS col2 FROM tab2 AS cor0
----
28

query IIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab1 AS cor0, tab1 AS cor1
----
972 values hashing to fe55095fff3a5ecc2f113d14a8c6f823

query I rowsort
SELECT distinct col1 * col1 - col1 AS col0 FROM tab1
----
156
650
90

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab2 AS cor0
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab1 cor1
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query III rowsort
SELECT * FROM tab1 cor0
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab0 AS cor0, tab1 cor1
----
243 values hashing to 9ed1a6a444254225f040123c46b7f70c

query I rowsort
SELECT col1 FROM tab1
----
10
13
26

query IIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query IIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab1 AS cor1
----
243 values hashing to 9ed1a6a444254225f040123c46b7f70c

query IIIIII rowsort
SELECT * FROM tab0 cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

query IIIIII rowsort
SELECT * FROM tab0 cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query I rowsort
SELECT col0 AS col2 FROM tab1 AS cor0
----
3
64
80

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query I rowsort
SELECT distinct 55 AS col0 FROM tab0
----
55

query I rowsort
SELECT ALL + col2 AS col2 FROM tab1
----
54
57
96

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 AS cor0, tab2 AS cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT 57 * ( col1 ) AS col0 FROM tab1 AS cor0
----
1482
570
741

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2, tab0 AS cor0
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query IIIIII rowsort
SELECT * FROM tab2, tab0 cor0
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query IIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query I rowsort
SELECT distinct col2 AS col2 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT ALL - col1 * - cor0.col0 - 13 AS col1 FROM tab1 AS cor0
----
1027
627
65

query I rowsort
SELECT ALL - - cor0.col2 + cor0.col1 FROM tab0 AS cor0
----
119
173
98

query I rowsort
SELECT ALL + col0 + - col0 FROM tab0 cor0
----
0
0
0

query III rowsort
SELECT distinct * FROM tab1 cor0
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query IIIIII rowsort
SELECT distinct * FROM tab2, tab0 AS cor0
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query I rowsort
SELECT col0 FROM tab0
----
24
35
89

query I rowsort
SELECT - - col0 * cor0.col2 + - col0 AS col1 FROM tab0 AS cor0
----
0
7209
768

query I rowsort
SELECT - col0 + col1 * - 42 * - col1 AS col0 FROM tab1 AS cor0
----
28389
4136
7018

query I rowsort
SELECT distinct col0 * 1 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT ALL - - col0 AS col0 FROM tab2 cor0
----
7
78
79

query I rowsort
SELECT col1 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT col1 * col0 FROM tab1 AS cor0
----
1040
640
78

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab2 AS cor1
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

query I rowsort
SELECT col0 AS col2 FROM tab0 AS cor0
----
24
35
89

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 AS cor0, tab0 AS cor1
----
243 values hashing to b3323704f6873113d863f8e27386b356

query I rowsort
SELECT distinct - - col0 * col2 AS col0 FROM tab0 AS cor0
----
35
7298
792

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0, tab2 AS cor1
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 cor0, tab0 AS cor1
----
243 values hashing to b3323704f6873113d863f8e27386b356

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab1 AS cor1
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 cor0, tab0 AS cor1
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query IIIIIIIIIIIIIII rowsort
SELECT distinct * FROM tab1 AS cor0 CROSS JOIN tab1, tab0 AS cor1, tab0 AS cor2, tab0 cor3
----
3645 values hashing to 181d902c42955a43a374f13a73d8b0a1

query IIIIIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab0, tab2 AS cor1, tab0 AS cor2
----
972 values hashing to 9345325155d9f4d7dc4986690c631cb9

query IIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

query I rowsort
SELECT - - cor0.col0 FROM tab0 AS cor0
----
24
35
89

query IIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query I rowsort
SELECT distinct 79 FROM tab0
----
79

query IIIIII rowsort
SELECT * FROM tab1 cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query IIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab2 cor1
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query IIIIII rowsort
SELECT distinct * FROM tab1 AS cor0 CROSS JOIN tab1 cor1
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query I rowsort
SELECT 21 * col0 + 85 FROM tab1
----
1429
148
1765

query IIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab2 cor1
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

query IIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query I rowsort
SELECT col2 * col0 AS col2 FROM tab2
----
189
2028
3002

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab0 cor1
----
243 values hashing to 3a953203ced079e372111d61dbd9e35f

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab1 cor0, tab0 cor1
----
972 values hashing to 67c5300bc5cba0be4f54a444dc6f05b9

query IIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab0 cor1
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab1 cor0
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query I rowsort
SELECT - tab2.col1 * ( - col0 ) FROM tab2
----
1343
217
4602

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0, tab1 AS cor0
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query I rowsort
SELECT distinct col0 * - col1 * ( - col1 ) FROM tab0 AS cor0
----
177504
329315
737009

query I rowsort
SELECT ALL - - col2 + col1 * 49 AS col0 FROM tab2 AS cor0
----
1546
2917
871

query III rowsort
SELECT * FROM tab2 cor0
----
9 values hashing to ad05b5942400d5e7a21b323b3da65a45

query I rowsort
SELECT - - 49 * col2 AS col0 FROM tab2 cor0
----
1274
1323
1862

query I rowsort
SELECT cor1.col2 AS col2 FROM tab2, tab0 AS cor0, tab1 AS cor1
----
27 values hashing to 7f4a9bf24d64833706dfbdd0baf49d79

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0 CROSS JOIN tab0 AS cor1
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query IIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query I rowsort
SELECT distinct tab0.col2 AS col0 FROM tab0
----
1
33
82

query I rowsort
SELECT col1 FROM tab2
----
17
31
59

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0 CROSS JOIN tab1, tab2 AS cor1
----
972 values hashing to 0fcd8d0934383dd58863be894b07a6ed

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col1 col0 FROM tab0
----
86
91
97

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab2 AS cor0
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT ( col1 ) * 8 FROM tab2
----
136
248
472

query I rowsort
SELECT col0 AS col2 FROM tab2
----
7
78
79

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1, tab2 AS cor0
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query I rowsort
SELECT distinct col0 * col1 AS col0 FROM tab1
----
1040
640
78

query I rowsort
SELECT col1 * cor0.col2 + - 22 AS col2 FROM tab0 AS cor0
----
2816
7440
75

query IIIIII rowsort
SELECT * FROM tab0, tab2 cor0
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

query I rowsort
SELECT - - cor0.col2 FROM tab2, tab0, tab2 AS cor0
----
27 values hashing to 40fd8cc0de92ea68d73634c2d8f75bf5

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0, tab1 AS cor0
----
243 values hashing to 70c6a01760d7239f3003db4da92180a4

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab1 AS cor1
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query I rowsort
SELECT ALL + col0 AS col2 FROM tab1
----
3
64
80

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL - col1 * - col1 col1 FROM tab2
----
289
3481
961

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 col1 FROM tab1
----
3
64
80

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0, tab2 AS cor1
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1, tab0 cor0, tab0
----
972 values hashing to 8b4fcda7f1ca76bad7c7d728f54a51e0

query I rowsort
SELECT col2 - - col1 AS col0 FROM tab2
----
55
58
85

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab1 cor0
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab0 AS cor0
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query III rowsort
SELECT distinct * FROM tab0 cor0
----
9 values hashing to 38a1673e2e09d694c8cec45c797034a7

query IIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query I rowsort
SELECT distinct col0 * tab1.col0 FROM tab1
----
4096
6400
9

query I rowsort
SELECT col0 FROM tab0 AS cor0
----
24
35
89

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab2 AS cor1
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

query I rowsort
SELECT cor0.col0 AS col0 FROM tab0, tab0 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab1 cor1
----
243 values hashing to 2464a6f4cfabe66aeca50fcb4cd85bf5

query I rowsort
SELECT ALL + col0 * col0 AS col0 FROM tab0 AS cor0
----
1225
576
7921

query I rowsort
SELECT - - col2 FROM tab0 AS cor0
----
1
33
82

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab0 cor0, tab1 AS cor1
----
243 values hashing to 9ed1a6a444254225f040123c46b7f70c

query I rowsort
SELECT - - ( col2 ) FROM tab0 cor0
----
1
33
82

query I rowsort
SELECT col0 - - col0 AS col1 FROM tab2 AS cor0
----
14
156
158

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab0 AS cor0
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

query I rowsort
SELECT col2 AS col1 FROM tab2
----
26
27
38

query I rowsort
SELECT ALL + cor0.col0 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT distinct - - col0 FROM tab2 cor0
----
7
78
79

query I rowsort
SELECT 38 * cor0.col0 FROM tab0 AS cor0
----
1330
3382
912

query I rowsort
SELECT - - col2 AS col0 FROM tab2 cor0
----
26
27
38

query I rowsort
SELECT distinct col2 AS col0 FROM tab2 AS cor0
----
26
27
38

query IIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query I rowsort
SELECT cor0.col0 AS col1 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT distinct col2 + cor0.col1 FROM tab1 AS cor0
----
109
67
80

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab0 AS cor1
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query IIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab2 cor1
----
243 values hashing to ce53c0e8839c969b0513568da6eb2c4b

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab2 AS cor1, tab2 AS cor2
----
972 values hashing to 82def1c3361e635dd4cf447edc22edb9

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0, tab0 AS cor1, tab0 AS cor2
----
972 values hashing to ea0f747588ddf5869ee18a5e22d9f237

query I rowsort
SELECT col1 * col1 FROM tab2
----
289
3481
961

query I rowsort
SELECT distinct col2 + ( col0 * tab1.col2 ) FROM tab1
----
216
3705
7776

query I rowsort
SELECT - 47 + col1 * tab1.col0 AS col0 FROM tab1
----
31
593
993

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - 38 * - col0 col0 FROM tab2
----
266
2964
3002

query IIIIII rowsort
SELECT * FROM tab2, tab2 cor0
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1, tab0 cor0
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab1 AS cor0
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab0 cor0
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab1 AS cor0, tab2 AS cor1
----
972 values hashing to 0fcd8d0934383dd58863be894b07a6ed

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 cor0, tab0 AS cor1
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab2 AS cor1
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query IIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab2, tab2 AS cor1
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query IIIIII rowsort
SELECT * FROM tab0 cor0 CROSS JOIN tab0 cor1
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query I rowsort
SELECT col2 AS col0 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT cor0.col2 FROM tab1 AS cor0
----
54
57
96

query IIIIII rowsort
SELECT * FROM tab0 cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query I rowsort
SELECT col1 FROM tab0 AS cor0
----
86
91
97

query IIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 AS cor0, tab1 AS cor1
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query I rowsort
SELECT 62 FROM tab1 AS cor0
----
62

query IIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT 51 + col2 * ( col0 ) col0 FROM tab2 AS cor0
----
2079
240
3053

query I rowsort
SELECT col1 + col1 AS col1 FROM tab0 AS cor0
----
172
182
194

query I rowsort
SELECT - - cor0.col1 AS col2 FROM tab0 AS cor0
----
86
91
97

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab0 AS cor1
----
243 values hashing to 3a953203ced079e372111d61dbd9e35f

query IIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query I rowsort
SELECT distinct - col2 + 49 FROM tab2
----
11
22
23

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0, tab2 AS cor1
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT - 14 + - col2 * - col0 AS col1 FROM tab2 AS cor0
----
175
2014
2988

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 AS cor0, tab2 AS cor1
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query I rowsort
SELECT tab1.col0 FROM tab1
----
3
64
80

query I rowsort
SELECT col2 FROM tab2
----
26
27
38

query I rowsort
SELECT col0 AS col0 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT col2 AS col1 FROM tab0 cor0
----
1
33
82

query I rowsort
SELECT distinct col1 * 55 FROM tab1 AS cor0
----
1430
550
715

query IIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab2 AS cor1
----
243 values hashing to 5ac29bd6e3a9e69ed9c73ca7a34114f7

query IIIIIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab1, tab2 AS cor1
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab1 AS cor1
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0, tab0 AS cor1
----
243 values hashing to 3a953203ced079e372111d61dbd9e35f

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2, tab0 AS cor0
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query I rowsort
SELECT ALL + 50 AS col1 FROM tab0
----
50

query I rowsort
SELECT ( col2 + col0 ) FROM tab0
----
171
36
57

query I rowsort
SELECT ALL + col2 AS col1 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT ALL + col0 AS col2 FROM tab2
----
7
78
79

query I rowsort
SELECT ALL + 90 AS col0 FROM tab1
----
90

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0, tab2 AS cor1
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query IIIIII rowsort
SELECT distinct * FROM tab1 AS cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query I rowsort
SELECT distinct col0 AS col1 FROM tab1
----
3
64
80

query I rowsort
SELECT col0 FROM tab2
----
7
78
79

query I rowsort
SELECT tab1.col1 + col0 FROM tab1
----
29
74
93

query I rowsort
SELECT col2 * col2 + col1 * tab2.col0 FROM tab2
----
2787
5278
946

query I rowsort
SELECT col1 AS col0 FROM tab2
----
17
31
59

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct cor0.col1 col2 FROM tab1, tab0 AS cor0
----
86
91
97

query I rowsort
SELECT distinct col1 + col1 FROM tab0 AS cor0
----
172
182
194

query I rowsort
SELECT distinct col2 AS col0 FROM tab0 AS cor0
----
1
33
82

query IIIIII rowsort
SELECT distinct * FROM tab2, tab1 AS cor0
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 cor0, tab0 AS cor1
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

query I rowsort
SELECT ALL + col1 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT distinct col2 + - col2 FROM tab1 cor0
----
0

query I rowsort
SELECT - - cor0.col2 + cor0.col0 + col2 FROM tab2 cor0
----
130
155
61

query I rowsort
SELECT ALL + 69 FROM tab1 cor0
----
69

query I rowsort
SELECT distinct - - cor0.col1 + col1 FROM tab1 AS cor0
----
20
26
52

query I rowsort
SELECT ( col2 ) FROM tab2
----
26
27
38

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0, tab0 cor1
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab2 AS cor0
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT distinct - - 84 + col1 * col2 + - col0 FROM tab1 AS cor0
----
1252
1485
590

query I rowsort
SELECT col2 FROM tab2 cor0
----
26
27
38

query I rowsort
SELECT ALL + col2 - col1 AS col0 FROM tab1 cor0
----
28
47
83

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0, tab2 AS cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query IIIIIIIII rowsort
SELECT * FROM tab2, tab2 cor0, tab2 AS cor1
----
243 values hashing to 5ac29bd6e3a9e69ed9c73ca7a34114f7

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab0 AS cor0
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query I rowsort
SELECT ALL + col2 + - col2 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT tab1.col0 AS col2 FROM tab1
----
3
64
80

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0, tab1 cor1, tab1 AS cor2
----
972 values hashing to fe55095fff3a5ecc2f113d14a8c6f823

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab2 AS cor0
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0, tab0 cor1
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query IIIIII rowsort
SELECT distinct * FROM tab0, tab2 cor0
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - 9 * - col2 col0 FROM tab1
----
486
513
864

query IIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab0 AS cor1
----
243 values hashing to b3323704f6873113d863f8e27386b356

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1, tab0 AS cor0
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query I rowsort
SELECT distinct - col2 * - col2 FROM tab2 AS cor0
----
1444
676
729

query I rowsort
SELECT distinct cor0.col2 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT ALL + ( col0 ) + - col0 FROM tab1
----
0
0
0

query I rowsort
SELECT col1 + - col0 AS col2 FROM tab0
----
2
62
62

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0, tab0 AS cor0
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query I rowsort
SELECT ALL - col0 + col0 AS col1 FROM tab1
----
0
0
0

query I rowsort
SELECT ALL + tab2.col1 AS col2 FROM tab2, tab1 AS cor0
----
9 values hashing to c61d27a0022e6d022371dc58819ab272

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab1 cor1
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query I rowsort
SELECT - tab1.col1 + - col1 * - tab1.col0 * col2 AS col0 FROM tab1
----
36470
4186
99827

query I rowsort
SELECT col0 * 35 AS col2 FROM tab1
----
105
2240
2800

query I rowsort
SELECT distinct col0 AS col2 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT col0 * 41 AS col1 FROM tab0 AS cor0
----
1435
3649
984

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - col1 + col2 * col2 col1 FROM tab2 AS cor0
----
1427
617
698

query I rowsort
SELECT col2 * 36 FROM tab1
----
1944
2052
3456

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab2 AS cor1
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1, tab2 cor0
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query IIIIII rowsort
SELECT distinct * FROM tab1, tab0 cor0
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query I rowsort
SELECT col0 FROM tab1
----
3
64
80

query I rowsort
SELECT tab2.col0 FROM tab2
----
7
78
79

query I rowsort
SELECT ALL + col2 AS col1 FROM tab2
----
26
27
38

query I rowsort
SELECT distinct col0 FROM tab2
----
7
78
79

query I rowsort
SELECT distinct tab0.col2 FROM tab0
----
1
33
82

query IIIIII rowsort
SELECT distinct * FROM tab1 AS cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0 cor0 CROSS JOIN tab2, tab2 AS cor1
----
972 values hashing to a698694a7dac245e42212ff0316bdf45

query I rowsort
SELECT col2 FROM tab1 AS cor0
----
54
57
96

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 col0 FROM tab1
----
3
64
80

query I rowsort
SELECT distinct col0 FROM tab0
----
24
35
89

query I rowsort
SELECT ALL + 97 * col0 AS col2 FROM tab1 AS cor0
----
291
6208
7760

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 AS cor0, tab1 AS cor1
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query I rowsort
SELECT cor0.col0 AS col0 FROM tab1 AS cor0
----
3
64
80

query IIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab2, tab2 AS cor1
----
972 values hashing to 163d7732097d78f1cda7f65c2cea5a08

query I rowsort
SELECT distinct tab0.col1 AS col0 FROM tab0, tab2 cor0
----
86
91
97

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0, tab2 AS cor1, tab0 AS cor2
----
972 values hashing to 86dbd337f00ab84c613ad03d6fc06e28

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 cor0, tab1 cor1
----
243 values hashing to 2464a6f4cfabe66aeca50fcb4cd85bf5

query I rowsort
SELECT ALL + col1 + - 3 AS col1 FROM tab1 cor0
----
10
23
7

query I rowsort
SELECT distinct - col1 + col2 FROM tab1 AS cor0
----
28
47
83

query I rowsort
SELECT - 2 * col1 * - col1 + - col1 - col1 * - col2 FROM tab1 AS cor0
----
1573
2730
760

query I rowsort
SELECT ALL - - col1 + col2 FROM tab0 cor0
----
119
173
98

query I rowsort
SELECT ALL - col2 + col1 FROM tab0 AS cor0
----
53
9
96

query I rowsort
SELECT ALL + col0 AS col2 FROM tab2 AS cor0
----
7
78
79

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 cor0, tab0 AS cor1
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query I rowsort
SELECT col2 FROM tab0
----
1
33
82

query I rowsort
SELECT ALL + 72 AS col2 FROM tab0 cor0
----
72

query I rowsort
SELECT distinct cor0.col1 * col2 FROM tab2 AS cor0
----
1534
646
837

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2, tab1 AS cor0
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab2 cor0
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

query I rowsort
SELECT ALL - col0 * - col1 * 23 + 7 FROM tab2
----
105853
30896
4998

query I rowsort
SELECT distinct tab1.col2 AS col2 FROM tab1
----
54
57
96

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab1 AS cor0
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query I rowsort
SELECT distinct - ( - col2 * col2 ) + col0 * col1 + 60 * col1 * col0 FROM tab0
----
126993
207096
500763

query I rowsort
SELECT col0 * col1 FROM tab2
----
1343
217
4602

query I rowsort
SELECT ALL + col1 * 47 FROM tab1 AS cor0
----
1222
470
611

query I rowsort
SELECT 5 AS col0 FROM tab2 cor0
----
5

query I rowsort
SELECT distinct col1 AS col2 FROM tab1
----
10
13
26

query I rowsort
SELECT col0 - col2 * - col0 FROM tab0 AS cor0
----
70
7387
816

query I rowsort
SELECT distinct - cor0.col2 + col1 * col2 AS col2 FROM tab1 AS cor0
----
1152
1350
513

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL - ( col0 ) + col1 col2 FROM tab0 AS cor0
----
2
62
62

query I rowsort
SELECT distinct col0 + - col0 AS col1 FROM tab2
----
0

query I rowsort
SELECT ALL + col0 AS col1 FROM tab0
----
24
35
89

query IIIIII rowsort
SELECT * FROM tab0, tab0 cor0
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query I rowsort
SELECT - col2 + cor0.col1 + - col0 * - col2 AS col1 FROM tab0 AS cor0
----
131
7307
845

query I rowsort
SELECT tab2.col0 + col0 + col1 FROM tab2
----
175
215
45

query I rowsort
SELECT - tab0.col2 + col1 FROM tab0
----
53
9
96

query III rowsort
SELECT * FROM tab1 WHERE NULL NOT IN ( col0 * col0 )
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query I rowsort
SELECT col2 + col0 FROM tab1
----
121
176
57

query I rowsort
SELECT distinct col2 * col0 FROM tab0
----
35
7298
792

query I rowsort
SELECT ALL + col2 + tab2.col0 * col0 FROM tab2
----
6110
6279
76

query I rowsort
SELECT col0 + - col0 FROM tab0
----
0
0
0

query I rowsort
SELECT ALL + tab0.col2 * col1 FROM tab0
----
2838
7462
97

query I rowsort
SELECT - - cor0.col0 AS col1 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT distinct col0 * col0 AS col0 FROM tab2 AS cor0
----
49
6084
6241

query I rowsort
SELECT ALL + cor0.col0 + col1 AS col2 FROM tab0 cor0
----
110
132
180

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col2 + col1 * col0 col1 FROM tab2 AS cor0
----
1381
244
4628

query I rowsort
SELECT distinct col0 + col0 FROM tab2 AS cor0
----
14
156
158

query I rowsort
SELECT distinct - - cor0.col1 AS col1 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT col2 FROM tab1 cor0
----
54
57
96

query I rowsort
SELECT ALL + col0 * cor0.col1 FROM tab0 cor0
----
2064
3395
8099

query I rowsort
SELECT tab2.col1 FROM tab2
----
17
31
59

query I rowsort
SELECT col1 AS col1 FROM tab0
----
86
91
97

query I rowsort
SELECT col0 + col0 AS col1 FROM tab1 AS cor0
----
128
160
6

query I rowsort
SELECT ALL + tab1.col1 * col1 + col2 * col1 AS col0 FROM tab1
----
1417
2080
670

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab2 WHERE NOT ( NULL ) >= NULL
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query I rowsort
SELECT tab2.col2 + col1 FROM tab2
----
55
58
85

query I rowsort
SELECT distinct cor0.col0 AS col2 FROM tab2, tab1 AS cor0
----
3
64
80

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + cor0.col1 col2 FROM tab1 AS cor0 CROSS JOIN tab1
----
9 values hashing to 366ec539af0f37bd1519bc568f3d6775

query I rowsort
SELECT col1 AS col0 FROM tab0
----
86
91
97

query I rowsort
SELECT distinct col0 FROM tab1
----
3
64
80

query I rowsort
SELECT ALL + cor1.col1 FROM tab1, tab2 AS cor0, tab0 cor1
----
27 values hashing to 2d6d3031dfe90e0c02db13aa63993bfd

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab2 cor0, tab2 AS cor1
----
972 values hashing to a47a9db07c7de4927c7c28efb4cd13f2

query I rowsort
SELECT - col0 - 85 * - col2 FROM tab1 AS cor0
----
4587
4781
8080

query I rowsort
SELECT distinct col1 AS col1 FROM tab1
----
10
13
26

query I rowsort
SELECT ALL + tab0.col1 AS col2 FROM tab0
----
86
91
97

query I rowsort
SELECT col1 * col1 + tab1.col2 AS col1 FROM tab1
----
157
265
730

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 * col2 col0 FROM tab1
----
1248
1404
570

query I rowsort
SELECT distinct col2 FROM tab2
----
26
27
38

query I rowsort
SELECT ALL + col0 AS col1 FROM tab1
----
3
64
80

query I rowsort
SELECT col0 AS col1 FROM tab0
----
24
35
89

query I rowsort
SELECT ALL + col1 AS col2 FROM tab0
----
86
91
97

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 cor0, tab0 AS cor1
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + cor0.col0 col2 FROM tab1, tab2 cor0
----
9 values hashing to 95b96ca1dbe2e39a0fa78f50d374f51a

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT distinct col0 - - col1 AS col0 FROM tab2 AS cor0
----
137
38
96

query I rowsort
SELECT ALL - col0 * - 64 + - col1 FROM tab0 AS cor0
----
1450
2143
5605

query I rowsort
SELECT ALL + col2 AS col2 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT col1 AS col1 FROM tab2
----
17
31
59

query I rowsort
SELECT col0 + col1 FROM tab2 AS cor0
----
137
38
96

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 * - ( - col2 ) col1 FROM tab1
----
162
3648
7680

query I rowsort
SELECT col0 AS col2 FROM tab0
----
24
35
89

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0, tab2 AS cor0
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT - col0 + col1 AS col0 FROM tab0
----
2
62
62

query I rowsort
SELECT ALL + col1 AS col2 FROM tab0 AS cor0
----
86
91
97

query IIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab0 cor1
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query I rowsort
SELECT distinct col0 AS col2 FROM tab1
----
3
64
80

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 cor0, tab0 cor1
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query IIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab0 cor1
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query I rowsort
SELECT col1 * cor0.col0 FROM tab2 AS cor0
----
1343
217
4602

query I rowsort
SELECT distinct col1 FROM tab2 AS cor0
----
17
31
59

query IIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab1, tab1 AS cor1
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query I rowsort
SELECT distinct - - col0 AS col1 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT distinct col2 + 64 + col0 FROM tab2 cor0
----
168
181
98

query I rowsort
SELECT - col0 * - 97 AS col0 FROM tab0 AS cor0
----
2328
3395
8633

query I rowsort
SELECT - col0 * - col2 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT ALL + cor0.col0 + ( col0 ) FROM tab1 AS cor0
----
128
160
6

query I rowsort
SELECT ALL + col1 AS col0 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT distinct - - 35 * 83 AS col1 FROM tab2 AS cor0
----
2905

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 AS cor0, tab0 AS cor1
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query I rowsort
SELECT distinct - - 81 AS col1 FROM tab1 AS cor0
----
81

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab0 AS cor0, tab1 AS cor1
----
243 values hashing to 9ed1a6a444254225f040123c46b7f70c

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL - - cor0.col2 col1 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT ALL + col1 AS col1 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT ALL + 62 * cor0.col1 FROM tab0 AS cor0
----
5332
5642
6014

query I rowsort
SELECT distinct cor0.col1 FROM tab1, tab2, tab0 AS cor0
----
86
91
97

query I rowsort
SELECT distinct col1 * col0 AS col0 FROM tab2
----
1343
217
4602

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1, tab1 cor0
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2, tab2 cor0
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query I rowsort
SELECT distinct 88 AS col1 FROM tab1
----
88

query I rowsort
SELECT tab1.col1 FROM tab1
----
10
13
26

query I rowsort
SELECT cor0.col0 FROM tab1, tab1 AS cor0
----
9 values hashing to dd18b93263a6cd425fc7cc84d9137870

query IIIIII rowsort
SELECT * FROM tab1, tab1 cor0
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0, tab1 AS cor1
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0 CROSS JOIN tab2, tab1 AS cor1
----
972 values hashing to 9364ef7545b07c67767dceb70f02c643

query I rowsort
SELECT ALL + 90 AS col2 FROM tab1
----
90

query IIIIII rowsort
SELECT distinct * FROM tab1, tab2 cor0
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query I rowsort
SELECT distinct ( col0 ) AS col2 FROM tab0
----
24
35
89

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab0 cor0, tab2 AS cor1
----
972 values hashing to 1e9d01970ae508486ddabec967bb176c

query I rowsort
SELECT col2 * col1 FROM tab1
----
1248
1404
570

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0, tab0 AS cor1
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1, tab2 AS cor0
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query I rowsort
SELECT col2 * tab0.col0 FROM tab0
----
35
7298
792

query I rowsort
SELECT col1 * ( 45 ) FROM tab2
----
1395
2655
765

query I rowsort
SELECT tab2.col2 AS col2 FROM tab2
----
26
27
38

query I rowsort
SELECT cor0.col0 AS col2 FROM tab0, tab2 cor0
----
9 values hashing to 95b96ca1dbe2e39a0fa78f50d374f51a

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab2 AS cor0, tab1 AS cor1
----
972 values hashing to 9364ef7545b07c67767dceb70f02c643

query I rowsort
SELECT col1 + - col1 AS col0 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT 31 FROM tab0
----
31

query I rowsort
SELECT col2 * 74 AS col1 FROM tab0 AS cor0
----
2442
6068
74

query I rowsort
SELECT 34 FROM tab0 AS cor0
----
34

query I rowsort
SELECT distinct col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT cor0.col1 AS col2 FROM tab2, tab0 AS cor0, tab2 AS cor1
----
27 values hashing to 2d6d3031dfe90e0c02db13aa63993bfd

query IIIIII rowsort
SELECT * FROM tab2, tab1 cor0
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0, tab1 AS cor1
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query I rowsort
SELECT ( 47 ) AS col1 FROM tab0
----
47

query I rowsort
SELECT ALL - col2 * - col1 FROM tab2
----
1534
646
837

query I rowsort
SELECT ALL + cor1.col0 FROM tab2, tab0 AS cor0, tab1 AS cor1
----
27 values hashing to 778b50575a9b91448119ee0ee1a9c44f

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 AS cor0, tab2 AS cor1
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query IIIIII rowsort
SELECT * FROM tab0, tab1 cor0
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query IIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab2 AS cor1
----
243 values hashing to ce53c0e8839c969b0513568da6eb2c4b

query I rowsort
SELECT 60 AS col1 FROM tab1 AS cor0
----
60

query I rowsort
SELECT col0 * col1 AS col0 FROM tab1 AS cor0
----
1040
640
78

query I rowsort
SELECT distinct - - col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT - - 25 FROM tab2 AS cor0
----
25

query I rowsort
SELECT 50 * cor0.col1 AS col1 FROM tab2 AS cor0
----
1550
2950
850

query IIIIII rowsort
SELECT * FROM tab1, tab0 cor0
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query I rowsort
SELECT distinct - - col1 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT distinct tab1.col2 AS col1 FROM tab1
----
54
57
96

query I rowsort
SELECT ALL + col1 + col1 FROM tab2 cor0
----
118
34
62

query I rowsort
SELECT - - col1 * 99 + col0 AS col2 FROM tab1 cor0
----
1054
1367
2577

query I rowsort
SELECT distinct col2 AS col0 FROM tab1
----
54
57
96

query I rowsort
SELECT ALL + col0 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT 98 - col2 AS col2 FROM tab2 AS cor0
----
60
71
72

query IIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab2 cor1
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

query I rowsort
SELECT ALL + col0 AS col2 FROM tab1 cor0
----
3
64
80

query I rowsort
SELECT ALL + tab0.col1 AS col0 FROM tab0, tab1 cor0
----
9 values hashing to 585a41a52c0c6c0d697b5d39265b74dc

query I rowsort
SELECT col0 + cor0.col1 AS col1 FROM tab2 cor0
----
137
38
96

query I rowsort
SELECT col2 AS col1 FROM tab0
----
1
33
82

query I rowsort
SELECT ALL + col0 FROM tab0
----
24
35
89

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab1 cor1, tab0 AS cor2
----
972 values hashing to 43f0c51511c8642d19190fd4dfcf905a

query I rowsort
SELECT col2 AS col2 FROM tab2
----
26
27
38

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 AS cor0, tab0 AS cor1
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

query I rowsort
SELECT ALL - col2 + - cor0.col1 * - col2 FROM tab2 AS cor0
----
1508
608
810

query I rowsort
SELECT col2 * 1 FROM tab1 AS cor0
----
54
57
96

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 + col1 col2 FROM tab1 AS cor0
----
109
67
80

query I rowsort
SELECT distinct ( col2 ) FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT ALL - - col2 AS col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT ALL + 30 * col2 FROM tab2
----
1140
780
810

query I rowsort
SELECT col0 AS col2 FROM tab2 cor0
----
7
78
79

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0, tab0 AS cor1
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

query I rowsort
SELECT - col0 * col0 * - 8 FROM tab0
----
4608
63368
9800

query I rowsort
SELECT distinct col1 + - col1 FROM tab1
----
0

query I rowsort
SELECT col1 + col0 FROM tab0
----
110
132
180

query I rowsort
SELECT col2 AS col0 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT distinct cor0.col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT ALL + col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT ALL - - col0 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT distinct - - 37 * col1 + col1 FROM tab2 AS cor0
----
1178
2242
646

query I rowsort
SELECT ALL + col1 FROM tab2 AS cor0
----
17
31
59

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2, tab2 AS cor0
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query I rowsort
SELECT ALL + cor0.col2 FROM tab0, tab2 AS cor0
----
9 values hashing to 5911bac51441f4ff640b2a2b721ea8e3

query IIIIIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0, tab1 AS cor1, tab2, tab2 AS cor2
----
3645 values hashing to 803a5565701c4ced6bba69940782c17a

query I rowsort
SELECT cor0.col1 FROM tab1 AS cor0
----
10
13
26

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0, tab2, tab2 AS cor1
----
972 values hashing to 64ce0e736818e884f0a9ecd075da5eb7

query I rowsort
SELECT distinct tab2.col2 FROM tab2
----
26
27
38

query I rowsort
SELECT ALL + col2 FROM tab0
----
1
33
82

query I rowsort
SELECT tab0.col0 FROM tab0
----
24
35
89

query I rowsort
SELECT col1 * cor0.col1 + 54 AS col0 FROM tab2 AS cor0
----
1015
343
3535

query I rowsort
SELECT cor0.col1 AS col0 FROM tab0 AS cor0
----
86
91
97

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1, tab1 AS cor0
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0, tab1 AS cor1
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query I rowsort
SELECT ALL + tab0.col1 AS col2 FROM tab0, tab1 AS cor0
----
9 values hashing to 585a41a52c0c6c0d697b5d39265b74dc

query I rowsort
SELECT ( col2 ) * col1 + col2 FROM tab2 cor0
----
1560
684
864

query I rowsort
SELECT distinct col2 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT col1 AS col0 FROM tab2 AS cor0
----
17
31
59

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab1 AS cor0
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query I rowsort
SELECT distinct col0 AS col1 FROM tab0
----
24
35
89

query I rowsort
SELECT col1 AS col0 FROM tab1
----
10
13
26

query I rowsort
SELECT col1 + - col1 AS col0 FROM tab2 AS cor0
----
0
0
0

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 col1 FROM tab2
----
7
78
79

query I rowsort
SELECT col2 + col2 AS col2 FROM tab2 AS cor0
----
52
54
76

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - col1 + col2 col1 FROM tab1 AS cor0
----
28
47
83

query I rowsort
SELECT col1 AS col1 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT - - col1 + 94 AS col0 FROM tab0 AS cor0
----
180
185
191

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 AS cor0 CROSS JOIN tab1
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query I rowsort
SELECT - col2 * - 73 AS col0 FROM tab0 cor0
----
2409
5986
73

query I rowsort
SELECT distinct 63 * cor0.col1 FROM tab0 AS cor0
----
5418
5733
6111

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab0, tab0 AS cor1
----
972 values hashing to 8b4fcda7f1ca76bad7c7d728f54a51e0

query I rowsort
SELECT col2 * 83 FROM tab1
----
4482
4731
7968

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab2 cor0
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT distinct - col0 * - 54 FROM tab1
----
162
3456
4320

query I rowsort
SELECT distinct - 76 * - 57 * col1 FROM tab0
----
372552
394212
420204

query I rowsort
SELECT ALL + col2 + col1 AS col0 FROM tab2 AS cor0
----
55
58
85

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0, tab2 AS cor1, tab2, tab1 AS cor2
----
3645 values hashing to a8d2ba8b8eb568b0a9a1771ccb0a8f23

query I rowsort
SELECT - 42 * - col0 FROM tab2 AS cor0
----
294
3276
3318

query I rowsort
SELECT distinct cor0.col2 * col2 * col2 AS col1 FROM tab0 AS cor0
----
1
35937
551368

query I rowsort
SELECT ( col0 ) AS col2 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT ALL + col0 * col1 FROM tab2
----
1343
217
4602

query I rowsort
SELECT tab1.col1 FROM tab1, tab1 AS cor0, tab2 AS cor1
----
27 values hashing to d671a064e2da709ca4cdfea317b8e892

query IIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab1 AS cor1
----
243 values hashing to 877a8dbac0e29b86e845fb64ed9d2242

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0, tab2, tab1 AS cor1
----
972 values hashing to 4c46de5c1773124597e14f3b372fc4ea

query I rowsort
SELECT distinct - - col1 AS col1 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT - col0 * - col0 FROM tab0 AS cor0
----
1225
576
7921

query I rowsort
SELECT ALL + ( col1 ) FROM tab2 AS cor0
----
17
31
59

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 cor0, tab2 AS cor1
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query I rowsort
SELECT distinct tab0.col1 + - col1 AS col1 FROM tab0
----
0

query I rowsort
SELECT col2 + col1 FROM tab1
----
109
67
80

query I rowsort
SELECT ALL - - col0 + col1 FROM tab0 AS cor0
----
110
132
180

query I rowsort
SELECT col2 AS col2 FROM tab1 AS cor0
----
54
57
96

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 AS cor0, tab1 AS cor1
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query I rowsort
SELECT col0 * col2 + - col0 AS col0 FROM tab1 AS cor0
----
159
3584
7600

query I rowsort
SELECT col0 * col1 AS col1 FROM tab0 cor0
----
2064
3395
8099

query I rowsort
SELECT ALL + col1 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT 52 AS col1 FROM tab1
----
52

query I rowsort
SELECT distinct col2 + col0 FROM tab2
----
104
117
34

query IIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab1, tab1 AS cor1
----
972 values hashing to a8481bfbfcb330825976c5896e54bc19

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 cor0, tab2 AS cor1
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query I rowsort
SELECT ALL + col0 AS col0 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT 38 + cor0.col2 FROM tab0, tab2 AS cor0
----
9 values hashing to 5d4444e709ceda9c70ea14e40445f143

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0, tab0 AS cor1, tab0 cor2
----
972 values hashing to 3406497351e4789c89a295ee9b64b201

query I rowsort
SELECT col2 FROM tab1
----
54
57
96

query IIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab1
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query IIIIII rowsort
SELECT * FROM tab0 cor0 CROSS JOIN tab0
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query I rowsort
SELECT col0 * col1 AS col1 FROM tab0
----
2064
3395
8099

query I rowsort
SELECT col0 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT col2 FROM tab0 AS cor0
----
1
33
82

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab1
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query III rowsort
SELECT * FROM tab0 WHERE NULL < ( NULL )
----

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col0 * col2 col0 FROM tab2
----
189
2028
3002

query IIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab0
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query I rowsort
SELECT col0 + cor0.col2 FROM tab2 AS cor0
----
104
117
34

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - cor0.col1 + col1 + col0 col1 FROM tab2 AS cor0
----
7
78
79

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col1 FROM tab0
----
86
91
97

query I rowsort
SELECT col2 AS col1 FROM tab1
----
54
57
96

query I rowsort
SELECT col0 * col1 AS col0 FROM tab1
----
1040
640
78

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1, tab0 AS cor0
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query I rowsort
SELECT col0 AS col0 FROM tab2
----
7
78
79

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab2 cor1
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

query I rowsort
SELECT ALL + col1 + col2 AS col2 FROM tab1
----
109
67
80

query III rowsort
SELECT distinct * FROM tab1 WHERE - col2 >= NULL
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query I rowsort
SELECT distinct tab2.col0 FROM tab2
----
7
78
79

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + tab2.col0 col0 FROM tab2
----
7
78
79

query I rowsort
SELECT ALL + col2 + col0 FROM tab1
----
121
176
57

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2, tab2 AS cor0
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

query I rowsort
SELECT - col0 + col2 + 68 FROM tab2 AS cor0
----
16
27
88

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab2 cor0
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT ALL + col2 FROM tab1
----
54
57
96

query I rowsort
SELECT col1 FROM tab0
----
86
91
97

query I rowsort
SELECT col0 AS col1 FROM tab1
----
3
64
80

query I rowsort
SELECT tab1.col2 FROM tab1
----
54
57
96

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct tab2.col1 col0 FROM tab2
----
17
31
59

query I rowsort
SELECT col1 + col2 FROM tab1
----
109
67
80

query I rowsort
SELECT col2 AS col0 FROM tab2
----
26
27
38

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 col0 FROM tab2
----
26
27
38

query I rowsort
SELECT distinct col1 AS col0 FROM tab0
----
86
91
97

query I rowsort
SELECT distinct col0 AS col1 FROM tab2
----
7
78
79

query I rowsort
SELECT col2 * col2 FROM tab1
----
2916
3249
9216

query I rowsort
SELECT col2 * col1 FROM tab0
----
2838
7462
97

query I rowsort
SELECT distinct col2 AS col1 FROM tab0
----
1
33
82

query I rowsort
SELECT ALL + col2 * tab0.col1 * col0 + - tab0.col2 FROM tab0
----
3394
664036
68079

query I rowsort
SELECT col2 - col2 AS col0 FROM tab2
----
0
0
0

query I rowsort
SELECT col2 AS col2 FROM tab1
----
54
57
96

query I rowsort
SELECT distinct col2 FROM tab0
----
1
33
82

query I rowsort
SELECT 72 * col0 * tab2.col0 AS col1 FROM tab2
----
3528
438048
449352

query I rowsort
SELECT ALL + col2 * cor0.col1 FROM tab0 AS cor0
----
2838
7462
97

query I rowsort
SELECT distinct - - col1 + col2 FROM tab0 AS cor0
----
119
173
98

query I rowsort
SELECT col0 * cor0.col2 AS col2 FROM tab0 AS cor0
----
35
7298
792

query I rowsort
SELECT distinct col2 FROM tab0 cor0
----
1
33
82

query I rowsort
SELECT distinct col1 * - col1 * - col2 FROM tab1 AS cor0
----
16224
36504
5700

query I rowsort
SELECT distinct col0 + col2 FROM tab2 AS cor0
----
104
117
34

query I rowsort
SELECT ALL - col2 + cor0.col2 FROM tab1 cor0
----
0
0
0

query I rowsort
SELECT distinct - cor0.col1 * - cor0.col0 AS col0 FROM tab2 AS cor0
----
1343
217
4602

query I rowsort
SELECT cor0.col2 * col1 AS col2 FROM tab1 cor0
----
1248
1404
570

query I rowsort
SELECT distinct 96 * col1 FROM tab2 cor0
----
1632
2976
5664

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0, tab2, tab0 AS cor1
----
972 values hashing to 9345325155d9f4d7dc4986690c631cb9

query I rowsort
SELECT - col0 AS col2 FROM tab0 cor0
----
4294967207
4294967261
4294967272

query I rowsort
SELECT distinct col1 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT col0 + col2 + ( col2 ) * col2 FROM tab2 AS cor0
----
1561
763
780

query I rowsort
SELECT - col1 * - col0 + col2 + - 80 AS col0 FROM tab2 AS cor0
----
1301
164
4548

query I rowsort
SELECT ALL - col1 + col1 FROM tab1 AS cor0
----
0
0
0

query I rowsort
SELECT col1 * col1 FROM tab0 AS cor0
----
7396
8281
9409

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 AS cor0, tab1 cor1
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query IIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab1 cor1
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query IIIIIIIII rowsort
SELECT * FROM tab0, tab0 cor0, tab0 AS cor1
----
243 values hashing to 3e8bd9634a3f5947d8becd5f5799bb7f

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0, tab1 AS cor1
----
243 values hashing to 70c6a01760d7239f3003db4da92180a4

query I rowsort
SELECT ALL - col2 * - col0 + col0 * col2 FROM tab0 cor0
----
14596
1584
70

query I rowsort
SELECT distinct - ( col0 ) + cor0.col0 AS col2 FROM tab0 AS cor0
----
0

query I rowsort
SELECT col0 * tab1.col1 + col2 + tab1.col0 * 71 AS col2 FROM tab1
----
345
5241
6816

query I rowsort
SELECT tab1.col0 + col2 AS col0 FROM tab1
----
121
176
57

query I rowsort
SELECT ( - col0 ) * - col2 AS col2 FROM tab1
----
162
3648
7680

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab2 AS cor1, tab1, tab1 AS cor2
----
3645 values hashing to 3ef3d333138b2b558b77004bad9bdabc

query IIIIIIIIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 AS cor0, tab1 AS cor1, tab0, tab0 AS cor2
----
3645 values hashing to 862fba9ac85fdf2cec88a0bec0808b7e

query I rowsort
SELECT distinct - - ( col2 ) FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT distinct - - col0 - col0 FROM tab1 AS cor0
----
0

query I rowsort
SELECT 92 FROM tab0
----
92

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col2 col2 FROM tab0
----
1
33
82

query I rowsort
SELECT - - col1 AS col0 FROM tab2 AS cor0
----
17
31
59

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab1 AS cor1, tab0 AS cor2
----
972 values hashing to e84152c0bf436177d3b3d80e42832d4f

query IIIIIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 cor0, tab0 AS cor1, tab2, tab2 AS cor2
----
3645 values hashing to f8426cd4d01ba96a72d7348574fbbc8e

query I rowsort
SELECT col0 AS col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT 55 AS col0 FROM tab1
----
55

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab0 AS cor1
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query I rowsort
SELECT cor1.col0 FROM tab1, tab1 AS cor0, tab0 AS cor1
----
27 values hashing to 9fc1dcd76feaf43e5c5dc060a02014cd

query IIIIIIIII rowsort
SELECT * FROM tab0, tab0 cor0, tab2 AS cor1
----
243 values hashing to ce53c0e8839c969b0513568da6eb2c4b

query I rowsort
SELECT - col0 * - col2 AS col2 FROM tab1 AS cor0
----
162
3648
7680

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 cor0, tab2 AS cor1
----
243 values hashing to d489341cd587fd6eb0b972c5464c6ddc

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 col1 FROM tab0
----
24
35
89

query I rowsort
SELECT tab2.col2 AS col0 FROM tab2, tab2 AS cor0
----
9 values hashing to 5911bac51441f4ff640b2a2b721ea8e3

query I rowsort
SELECT 41 * col1 AS col1 FROM tab0
----
3526
3731
3977

query I rowsort
SELECT distinct col2 AS col0 FROM tab2
----
26
27
38

query I rowsort
SELECT distinct - 50 * - col0 + - col0 AS col0 FROM tab1 AS cor0
----
147
3136
3920

query I rowsort
SELECT ALL - tab0.col2 + - 98 AS col2 FROM tab0
----
4294967116
4294967165
4294967197

query I rowsort
SELECT col1 + col1 FROM tab2
----
118
34
62

query I rowsort
SELECT - col0 * - col1 + col2 AS col1 FROM tab1 AS cor0
----
1136
132
697

query I rowsort
SELECT distinct 90 + col0 FROM tab2
----
168
169
97

query I rowsort
SELECT col0 + col2 FROM tab2
----
104
117
34

query I rowsort
SELECT cor1.col2 FROM tab0, tab0 AS cor0, tab1 AS cor1
----
27 values hashing to 7f4a9bf24d64833706dfbdd0baf49d79

query I rowsort
SELECT - col2 * - tab2.col2 FROM tab2
----
1444
676
729

query I rowsort
SELECT distinct cor0.col1 FROM tab0, tab1 AS cor0
----
10
13
26

query I rowsort
SELECT cor0.col2 * ( cor0.col2 ) - - cor0.col1 FROM tab1 AS cor0
----
2942
3259
9229

query I rowsort
SELECT distinct col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT col0 AS col1 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT col1 AS col2 FROM tab0
----
86
91
97

query I rowsort
SELECT distinct 99 AS col1 FROM tab0
----
99

query I rowsort
SELECT ALL + 79 FROM tab2
----
79

query I rowsort
SELECT distinct - col1 * - 58 FROM tab1 AS cor0
----
1508
580
754

query I rowsort
SELECT distinct - - col2 + 19 * col2 AS col2 FROM tab1 cor0
----
1080
1140
1920

query I rowsort
SELECT distinct - col1 + ( - cor0.col2 ) * - col0 AS col1 FROM tab2 AS cor0
----
158
1969
2985

query I rowsort
SELECT cor0.col0 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT distinct col1 + col0 AS col2 FROM tab2
----
137
38
96

query I rowsort
SELECT ALL - col2 + - 58 * col1 * - col2 AS col2 FROM tab0
----
164571
432714
5625

query I rowsort
SELECT col2 - - col1 AS col2 FROM tab1 AS cor0
----
109
67
80

query I rowsort
SELECT col1 + col2 FROM tab1 AS cor0
----
109
67
80

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab0 AS cor0, tab2 cor1
----
243 values hashing to ce53c0e8839c969b0513568da6eb2c4b

query I rowsort
SELECT ALL + col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT 98 * col2 FROM tab2 AS cor0
----
2548
2646
3724

query I rowsort
SELECT distinct col1 AS col0 FROM tab2 AS cor0
----
17
31
59

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab2 AS cor1, tab0 AS cor2
----
972 values hashing to 9a5ab925af18e11f7748f3b2e722ff3d

query I rowsort
SELECT ALL + col2 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT 48 * col0 AS col2 FROM tab2 AS cor0
----
336
3744
3792

query IIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab0 AS cor1
----
243 values hashing to 3e8bd9634a3f5947d8becd5f5799bb7f

query I rowsort
SELECT 51 FROM tab2 AS cor0
----
51

query I rowsort
SELECT col0 AS col1 FROM tab2
----
7
78
79

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 AS cor0, tab1 cor1
----
243 values hashing to 877a8dbac0e29b86e845fb64ed9d2242

query IIIIIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab1, tab1 AS cor1
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query I rowsort
SELECT tab2.col1 AS col2 FROM tab2
----
17
31
59

query IIIIIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab0, tab1 AS cor1
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 cor0, tab0 AS cor1
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query I rowsort
SELECT distinct col2 AS col1 FROM tab1 AS cor0
----
54
57
96

query IIIIIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab0 AS cor1, tab0, tab0 AS cor2
----
3645 values hashing to db9b93cf4fdd5de4106f0487a66ce0a5

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab0 AS cor1
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - col1 + col1 + cor0.col0 col1 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT distinct 28 + - col1 AS col2 FROM tab1 AS cor0
----
15
18
2

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 cor0, tab2 cor1
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT distinct - col0 + col0 AS col2 FROM tab1 AS cor0
----
0

query I rowsort
SELECT cor0.col0 AS col2 FROM tab0, tab0 cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 AS cor0, tab2 cor1
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0, tab2 AS cor1
----
243 values hashing to d489341cd587fd6eb0b972c5464c6ddc

query I rowsort
SELECT - ( - cor0.col0 ) FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT col1 + cor0.col2 * col1 FROM tab2 AS cor0
----
1593
663
868

query I rowsort
SELECT - col0 * 43 * - col1 FROM tab0
----
145985
348257
88752

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab0 cor0
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query I rowsort
SELECT ALL - col1 + col2 + col2 * col1 AS col0 FROM tab0
----
1
2785
7453

query I rowsort
SELECT distinct col2 * cor0.col2 AS col0 FROM tab2 cor0
----
1444
676
729

query I rowsort
SELECT ALL + - col2 + - col1 * ( col0 ) * - cor0.col1 AS col0 FROM tab1 AS cor0
----
13424
1974
6343

query I rowsort
SELECT - - col1 - col0 * - col1 AS col0 FROM tab2 AS cor0
----
1360
248
4661

query I rowsort
SELECT ALL + 77 AS col1 FROM tab0 cor0
----
77

query I rowsort
SELECT cor0.col2 * 35 FROM tab0 AS cor0
----
1155
2870
35

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - col2 * - col1 col0 FROM tab0 AS cor0
----
2838
7462
97

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col2 col1 FROM tab2 cor0
----
26
27
38

query I rowsort
SELECT col0 * col0 AS col1 FROM tab2
----
49
6084
6241

query I rowsort
SELECT col1 * 61 + col0 FROM tab2 AS cor0
----
1116
1898
3677

query I rowsort
SELECT distinct col1 AS col1 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT col1 AS col1 FROM tab1 AS cor0
----
10
13
26

query IIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab0 cor1
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query IIIIII rowsort
SELECT distinct * FROM tab1 AS cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0 CROSS JOIN tab2, tab0 AS cor1
----
972 values hashing to deaaa983f771be544ffdc26f04a18657

query I rowsort
SELECT col2 * col1 FROM tab1 AS cor0
----
1248
1404
570

query I rowsort
SELECT ALL + ( col2 ) AS col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT cor0.col2 AS col1 FROM tab1 AS cor0
----
54
57
96

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - col2 + col2 col2 FROM tab1
----
0
0
0

query I rowsort
SELECT col0 + ( col0 ) FROM tab0
----
178
48
70

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct ( - col0 + col0 ) col2 FROM tab2
----
0

query I rowsort
SELECT distinct col2 * tab2.col0 FROM tab2
----
189
2028
3002

query IIIIII rowsort
SELECT distinct * FROM tab1 cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query I rowsort
SELECT col2 AS col0 FROM tab1
----
54
57
96

query I rowsort
SELECT - - cor0.col1 AS col0 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ALL - - col1 - col1 FROM tab1 AS cor0
----
0
0
0

query I rowsort
SELECT - - 21 * col2 FROM tab1 AS cor0
----
1134
1197
2016

query I rowsort
SELECT distinct col1 - - col0 FROM tab2 AS cor0
----
137
38
96

query IIIIII rowsort
SELECT distinct * FROM tab0 cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query I rowsort
SELECT distinct - - col2 + cor0.col0 AS col2 FROM tab0 AS cor0
----
171
36
57

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct cor0.col1 col1 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT 87 AS col2 FROM tab1
----
87

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0, tab0 AS cor1
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query I rowsort
SELECT 4 AS col2 FROM tab2 AS cor0
----
4

query I rowsort
SELECT col1 AS col1 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT - - col0 + col1 AS col0 FROM tab2 AS cor0
----
137
38
96

query I rowsort
SELECT - - col1 FROM tab0 AS cor0
----
86
91
97

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab0 cor1, tab0 AS cor2
----
972 values hashing to 8420206d6932c454f05a38de634b3cb5

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col0 col0 FROM tab0
----
24
35
89

query IIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0, tab1, tab0 AS cor1
----
972 values hashing to 5e655b1287771868a8f868574a94d749

query I rowsort
SELECT cor0.col1 AS col1 FROM tab0, tab0 cor0
----
9 values hashing to 585a41a52c0c6c0d697b5d39265b74dc

query IIIIII rowsort
SELECT * FROM tab1 cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab0, tab2 AS cor1
----
972 values hashing to 591a9a93560839231c038a1e10bd240a

query I rowsort
SELECT distinct 5 + 30 AS col1 FROM tab2
----
35

query I rowsort
SELECT col1 AS col2 FROM tab1
----
10
13
26

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab0 AS cor0, tab2
----
972 values hashing to 1e9d01970ae508486ddabec967bb176c

query I rowsort
SELECT 42 FROM tab1
----
42

query I rowsort
SELECT distinct col2 AS col2 FROM tab1
----
54
57
96

query I rowsort
SELECT ALL - 36 FROM tab1
----
4294967260

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col1 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ALL + col1 AS col0 FROM tab2
----
17
31
59

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 cor0, tab2 AS cor1, tab1 AS cor2
----
972 values hashing to 980274175fafec015a83080672486a9a

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab0 AS cor0
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query I rowsort
SELECT - 2 * - 43 AS col1 FROM tab1 AS cor0
----
86

query I rowsort
SELECT - cor0.col1 - - col1 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT distinct - - 27 FROM tab1 AS cor0
----
27

query I rowsort
SELECT col1 + col0 FROM tab1 AS cor0
----
29
74
93

query I rowsort
SELECT 62 * col1 + - col0 FROM tab1 AS cor0
----
1609
556
726

query I rowsort
SELECT ALL - ( - 92 ) FROM tab2 AS cor0
----
92

query IIIIII rowsort
SELECT distinct * FROM tab2, tab1 cor0
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query I rowsort
SELECT col1 AS col0 FROM tab0 AS cor0
----
86
91
97

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab2 cor1
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT cor0.col2 + col0 col2 FROM tab0 AS cor0
----
171
36
57

query I rowsort
SELECT ALL - - col1 * col1 - col0 AS col1 FROM tab1 AS cor0
----
36
673
89

query I rowsort
SELECT ALL + col1 AS col1 FROM tab1
----
10
13
26

query I rowsort
SELECT distinct col1 FROM tab1
----
10
13
26

query I rowsort
SELECT distinct col0 AS col1 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT - - 62 AS col0 FROM tab2 AS cor0
----
62

query I rowsort
SELECT col2 AS col2 FROM tab0 AS cor0
----
1
33
82

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col1 + col0 col1 FROM tab1 AS cor0
----
29
74
93

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2, tab0 cor0, tab0
----
972 values hashing to 09b120a8ff13ebafea7af10c2152241b

query I rowsort
SELECT col0 AS col2 FROM tab2 AS cor0
----
7
78
79

query IIIIIIIII rowsort
SELECT * FROM tab0, tab0 cor0, tab0 cor1
----
243 values hashing to 3e8bd9634a3f5947d8becd5f5799bb7f

query I rowsort
SELECT ALL + col1 * col1 AS col1 FROM tab0 AS cor0
----
7396
8281
9409

query I rowsort
SELECT 55 + - 34 FROM tab1 AS cor0
----
21

query IIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab1, tab1 AS cor1
----
243 values hashing to 2464a6f4cfabe66aeca50fcb4cd85bf5

query IIIIIIIII rowsort
SELECT * FROM tab2 cor0 CROSS JOIN tab1, tab1 AS cor1
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query I rowsort
SELECT - - col1 + col1 FROM tab1 AS cor0
----
20
26
52

query I rowsort
SELECT distinct 9 * col1 AS col0 FROM tab2
----
153
279
531

query I rowsort
SELECT distinct 12 * col1 AS col1 FROM tab0
----
1032
1092
1164

query I rowsort
SELECT col2 + tab2.col1 FROM tab2
----
55
58
85

query I rowsort
SELECT distinct 51 + col2 * ( ( col2 ) ) * 0 AS col2 FROM tab1
----
51

query I rowsort
SELECT tab0.col0 AS col2 FROM tab0, tab0 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query IIIIIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab2, tab0 AS cor1
----
243 values hashing to b3323704f6873113d863f8e27386b356

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab0, tab1 AS cor1, tab2, tab2 AS cor2
----
3645 values hashing to b62c1ebc681aca72d13feadb888b3be7

query I rowsort
SELECT ALL + col1 * 27 AS col0 FROM tab2
----
1593
459
837

query I rowsort
SELECT ALL - cor0.col0 * - col1 + - col1 FROM tab2 AS cor0
----
1326
186
4543

query I rowsort
SELECT - - col2 - - 84 AS col2 FROM tab2 AS cor0
----
110
111
122

query I rowsort
SELECT 31 FROM tab1
----
31

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0, tab1 cor0
----
243 values hashing to 70c6a01760d7239f3003db4da92180a4

query I rowsort
SELECT col2 * col0 FROM tab1
----
162
3648
7680

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1, tab2 AS cor0
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query I rowsort
SELECT distinct col1 * 69 FROM tab0 AS cor0
----
5934
6279
6693

query I rowsort
SELECT ALL + col2 + - col0 AS col0 FROM tab2 AS cor0
----
20
4294967244
4294967255

query I rowsort
SELECT ALL + col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT - col1 * - 30 + col2 + - 53 FROM tab2 AS cor0
----
1743
495
904

query I rowsort
SELECT ALL - col0 * - 5 AS col1 FROM tab1
----
15
320
400

query I rowsort
SELECT distinct 76 * col0 * col0 AS col1 FROM tab1 AS cor0
----
311296
486400
684

query I rowsort
SELECT - col2 * - col1 FROM tab2 cor0
----
1534
646
837

query I rowsort
SELECT ALL + col2 FROM tab0 cor0
----
1
33
82

query I rowsort
SELECT ALL + 59 AS col0 FROM tab2 AS cor0
----
59

query I rowsort
SELECT ( 0 + tab0.col2 ) AS col2 FROM tab0
----
1
33
82

query I rowsort
SELECT distinct col0 * col2 FROM tab1
----
162
3648
7680

query I rowsort
SELECT ALL - - 31 * col0 AS col0 FROM tab0 AS cor0
----
1085
2759
744

query I rowsort
SELECT ALL + col1 + col1 FROM tab1
----
20
26
52

query I rowsort
SELECT ALL - col1 * - col2 FROM tab1
----
1248
1404
570

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 AS cor0, tab1 AS cor1
----
243 values hashing to 877a8dbac0e29b86e845fb64ed9d2242

query IIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab2, tab1 AS cor1
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query I rowsort
SELECT ALL + col0 AS col0 FROM tab2 AS cor0
----
7
78
79

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab0 AS cor0, tab0
----
972 values hashing to 09b120a8ff13ebafea7af10c2152241b

query I rowsort
SELECT - col1 * - ( col2 ) - - col1 * col1 FROM tab2
----
1798
5015
935

query I rowsort
SELECT distinct 3 * col2 FROM tab0
----
246
3
99

query I rowsort
SELECT ALL + col0 AS col2 FROM tab0 AS cor0
----
24
35
89

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab0 cor1
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query I rowsort
SELECT - col2 + col0 * col1 FROM tab2
----
1305
190
4576

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1, tab0 AS cor0, tab0
----
972 values hashing to 8b4fcda7f1ca76bad7c7d728f54a51e0

query I rowsort
SELECT col1 + - col1 AS col0 FROM tab2
----
0
0
0

query I rowsort
SELECT col0 * ( col1 ) FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT distinct col1 FROM tab2
----
17
31
59

query I rowsort
SELECT ALL + col1 AS col1 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT col2 + col2 AS col0 FROM tab1
----
108
114
192

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab0 AS cor0
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query I rowsort
SELECT ALL + col0 + col1 AS col0 FROM tab1
----
29
74
93

query I rowsort
SELECT ALL - col2 * col0 + 67 * col0 FROM tab2 AS cor0
----
2291
280
3198

query I rowsort
SELECT ALL + col2 * col0 AS col2 FROM tab1 AS cor0
----
162
3648
7680

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0, tab1 cor1
----
243 values hashing to 2464a6f4cfabe66aeca50fcb4cd85bf5

query I rowsort
SELECT ALL + - col1 + col0 * 32 FROM tab2 AS cor0
----
193
2437
2511

query I rowsort
SELECT cor0.col1 * col1 + 55 FROM tab2 AS cor0
----
1016
344
3536

query I rowsort
SELECT distinct - - 81 FROM tab1 AS cor0
----
81

query I rowsort
SELECT distinct col0 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT ( - tab0.col2 ) * - ( tab0.col2 ) FROM tab0
----
1
1089
6724

query I rowsort
SELECT distinct col0 * col1 FROM tab2
----
1343
217
4602

query I rowsort
SELECT distinct - - cor0.col2 FROM tab0 AS cor0
----
1
33
82

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0, tab2 cor1
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query I rowsort
SELECT distinct col0 * tab1.col2 FROM tab1
----
162
3648
7680

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col2 col2 FROM tab1 cor0
----
54
57
96

query I rowsort
SELECT ALL + col1 + col2 AS col0 FROM tab0
----
119
173
98

query I rowsort
SELECT ALL + 61 + col1 FROM tab1 cor0
----
71
74
87

query I rowsort
SELECT 92 FROM tab0 AS cor0
----
92

query I rowsort
SELECT ALL - ( - col2 ) * col1 FROM tab0 AS cor0
----
2838
7462
97

query I rowsort
SELECT col1 AS col2 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT - - ( col2 ) AS col1 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT col0 - col0 AS col2 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT - 15 * 0 FROM tab2
----
0

query I rowsort
SELECT cor0.col1 FROM tab2, tab1 AS cor0
----
9 values hashing to 366ec539af0f37bd1519bc568f3d6775

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0, tab2 cor0
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT ALL + col1 AS col2 FROM tab1
----
10
13
26

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct ( col2 ) col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT col0 * tab0.col0 + col0 - col1 FROM tab0
----
1163
514
7919

query IIIIII rowsort
SELECT * FROM tab1 cor0 CROSS JOIN tab0 cor1
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query I rowsort
SELECT 78 AS col0 FROM tab1 AS cor0
----
78

query I rowsort
SELECT col0 + 0 FROM tab2
----
7
78
79

query I rowsort
SELECT col0 * cor0.col1 FROM tab0 AS cor0
----
2064
3395
8099

query IIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab1, tab2 AS cor1
----
243 values hashing to d489341cd587fd6eb0b972c5464c6ddc

query I rowsort
SELECT col2 * 23 FROM tab1 AS cor0
----
1242
1311
2208

query I rowsort
SELECT col1 * 69 FROM tab0 AS cor0
----
5934
6279
6693

query I rowsort
SELECT distinct cor0.col1 AS col1 FROM tab0, tab2 AS cor0
----
17
31
59

query I rowsort
SELECT 85 - - col0 FROM tab2 AS cor0
----
163
164
92

query IIIIIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab2, tab1 AS cor1
----
243 values hashing to 877a8dbac0e29b86e845fb64ed9d2242

query I rowsort
SELECT distinct cor1.col0 FROM tab2, tab1 AS cor0, tab0 AS cor1
----
24
35
89

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab2 AS cor1
----
243 values hashing to d489341cd587fd6eb0b972c5464c6ddc

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab1 cor0
----
243 values hashing to 70c6a01760d7239f3003db4da92180a4

query I rowsort
SELECT ALL + col1 FROM tab2
----
17
31
59

query I rowsort
SELECT ALL + col0 * col2 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT distinct col0 + col0 AS col1 FROM tab2 AS cor0
----
14
156
158

query I rowsort
SELECT ALL + col1 + 44 FROM tab0 cor0
----
130
135
141

query I rowsort
SELECT distinct cor0.col1 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ( 0 ) * - col0 * 56 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT ALL + col1 AS col0 FROM tab1 cor0
----
10
13
26

query I rowsort
SELECT distinct tab2.col0 + - col2 * - col1 FROM tab2
----
1612
725
844

query I rowsort
SELECT ALL - ( - cor0.col1 ) * col1 AS col0 FROM tab0 cor0
----
7396
8281
9409

query I rowsort
SELECT distinct - - col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT - - 61 AS col0 FROM tab1 AS cor0
----
61

query I rowsort
SELECT - col2 * - col1 FROM tab0 AS cor0
----
2838
7462
97

query I rowsort
SELECT - col1 * col2 * - col2 AS col1 FROM tab2
----
22599
24548
39884

query I rowsort
SELECT distinct col1 * col2 + col0 AS col0 FROM tab0
----
132
2862
7551

query I rowsort
SELECT distinct - - cor0.col0 * col1 FROM tab1 AS cor0
----
1040
640
78

query I rowsort
SELECT distinct col1 * - col2 * - cor0.col1 FROM tab1 AS cor0
----
16224
36504
5700

query I rowsort
SELECT cor0.col1 FROM tab0, tab2, tab2 AS cor0
----
27 values hashing to 7599b480125de521efed71b5b2413c7d

query IIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab2, tab0 AS cor1
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query IIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab2, tab1 AS cor1
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query I rowsort
SELECT tab0.col2 FROM tab0
----
1
33
82

query I rowsort
SELECT col0 * col0 FROM tab0
----
1225
576
7921

query I rowsort
SELECT distinct 24 FROM tab1
----
24

query I rowsort
SELECT ( col2 ) FROM tab0
----
1
33
82

query I rowsort
SELECT - ( - 94 * col0 ) AS col2 FROM tab2
----
658
7332
7426

query I rowsort
SELECT - - 28 AS col1 FROM tab0 AS cor0
----
28

query I rowsort
SELECT 26 FROM tab2
----
26

query I rowsort
SELECT ALL - ( - col2 ) AS col0 FROM tab1
----
54
57
96

query I rowsort
SELECT distinct col1 AS col0 FROM tab1
----
10
13
26

query I rowsort
SELECT distinct col0 AS col2 FROM tab2
----
7
78
79

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2, tab0 AS cor0, tab2 AS cor1
----
972 values hashing to 89714dd446b7a97f8787d5744bdbf323

query I rowsort
SELECT 28 AS col1 FROM tab0 AS cor0
----
28

query I rowsort
SELECT 8 FROM tab0
----
8

query I rowsort
SELECT ALL - cor0.col2 * - col2 AS col0 FROM tab2 AS cor0
----
1444
676
729

query I rowsort
SELECT distinct cor0.col1 * 73 + - col1 * - col0 FROM tab1 cor0
----
1370
1976
1989

query I rowsort
SELECT 24 FROM tab2
----
24

query I rowsort
SELECT col2 * col0 FROM tab2 AS cor0
----
189
2028
3002

query I rowsort
SELECT 31 FROM tab0 AS cor0
----
31

query I rowsort
SELECT cor0.col2 AS col2 FROM tab1 AS cor0
----
54
57
96

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 AS cor0, tab2 cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT 55 * col1 AS col0 FROM tab2 AS cor0
----
1705
3245
935

query IIIIII rowsort
SELECT distinct * FROM tab0, tab0 cor0
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab2 AS cor0, tab2 AS cor1
----
972 values hashing to 163d7732097d78f1cda7f65c2cea5a08

query I rowsort
SELECT - col1 + col1 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT - 3 + col2 AS col0 FROM tab1
----
51
54
93

query IIIIII rowsort
SELECT distinct * FROM tab1, tab1 cor0
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

query I rowsort
SELECT distinct cor0.col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT - 56 * - 4 FROM tab1 AS cor0
----
224

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab0 AS cor0, tab2 AS cor1
----
972 values hashing to 42e69ecdafb3c81046bc5cb4c98b1666

query I rowsort
SELECT col1 AS col1 FROM tab1 cor0
----
10
13
26

query I rowsort
SELECT - 70 * - 39 + col0 FROM tab0 AS cor0
----
2754
2765
2819

query I rowsort
SELECT - - ( col2 ) FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT col2 * tab1.col1 FROM tab1
----
1248
1404
570

query I rowsort
SELECT ALL + 55 FROM tab0
----
55

query I rowsort
SELECT cor0.col0 AS col0 FROM tab0, tab1 AS cor0, tab1 AS cor1
----
27 values hashing to 778b50575a9b91448119ee0ee1a9c44f

query I rowsort
SELECT distinct - - 22 FROM tab0 cor0
----
22

query I rowsort
SELECT col0 AS col2 FROM tab1 cor0
----
3
64
80

query I rowsort
SELECT ( col1 ) FROM tab0 cor0
----
86
91
97

query I rowsort
SELECT ALL + ( cor0.col0 ) + col0 AS col2 FROM tab0 AS cor0
----
178
48
70

query I rowsort
SELECT ALL + cor0.col1 AS col0 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT ALL + - col2 + col2 FROM tab1 AS cor0
----
0
0
0

query IIIIIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab1, tab2 AS cor1
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query IIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab2 cor1
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query I rowsort
SELECT - - col2 + col2 + col0 AS col2 FROM tab2 AS cor0
----
130
155
61

query I rowsort
SELECT ALL - - cor0.col1 AS col0 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT - - cor0.col1 * 88 + - col2 * - col2 FROM tab1 AS cor0
----
10360
4129
5204

query I rowsort
SELECT ALL + col2 AS col0 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT ( cor0.col0 ) + col0 AS col0 FROM tab2 AS cor0
----
14
156
158

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + 72 + cor0.col2 col1 FROM tab2 AS cor0
----
110
98
99

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab1 cor1
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query IIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab1 cor1
----
243 values hashing to 9ed1a6a444254225f040123c46b7f70c

query IIIIIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab1, tab2 AS cor1
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query I rowsort
SELECT distinct cor0.col2 * col0 AS col1 FROM tab2 cor0
----
189
2028
3002

query I rowsort
SELECT - - col1 FROM tab1 cor0
----
10
13
26

query I rowsort
SELECT distinct col0 AS col0 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT ALL + col0 * cor0.col1 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT ALL - - cor0.col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT - col0 - - col0 FROM tab2 AS cor0
----
0
0
0

query I rowsort
SELECT - col1 + col1 AS col0 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT ALL - cor0.col1 * - col0 AS col0 FROM tab1 AS cor0
----
1040
640
78

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0, tab0 AS cor1, tab1 cor2
----
972 values hashing to 9af67d6f98010464af5d560bf949d487

query I rowsort
SELECT distinct col1 FROM tab1 cor0
----
10
13
26

query I rowsort
SELECT distinct ( col1 ) + - 20 AS col1 FROM tab0 cor0
----
66
71
77

query I rowsort
SELECT col2 * col0 + - col0 FROM tab2
----
182
1950
2923

query I rowsort
SELECT ALL + col1 + col2 AS col1 FROM tab0
----
119
173
98

query I rowsort
SELECT - col0 * - ( col0 ) FROM tab2 AS cor0
----
49
6084
6241

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab0 AS cor0, tab1 AS cor1
----
972 values hashing to 5621675b1bd32b061d284d0444c76601

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1, tab1 AS cor0
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query I rowsort
SELECT - col1 * - 3 FROM tab1 AS cor0
----
30
39
78

query I rowsort
SELECT ALL - col0 * - 98 - - col0 FROM tab2 AS cor0
----
693
7722
7821

query I rowsort
SELECT - 68 * - 99 FROM tab1 AS cor0
----
6732

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2, tab1 cor0, tab0
----
972 values hashing to 9b91cf9fcc064ee1c13074a678b72ac7

query I rowsort
SELECT 28 AS col0 FROM tab2
----
28

query I rowsort
SELECT cor0.col0 FROM tab0, tab2 AS cor0
----
9 values hashing to 95b96ca1dbe2e39a0fa78f50d374f51a

query I rowsort
SELECT distinct - 26 + col1 FROM tab0 AS cor0
----
60
65
71

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 cor0, tab0 AS cor1
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - col2 + col1 col0 FROM tab0 AS cor0
----
53
9
96

query I rowsort
SELECT distinct - - 72 FROM tab2 AS cor0
----
72

query I rowsort
SELECT ALL + tab2.col0 * col2 FROM tab2
----
189
2028
3002

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab0 AS cor0 WHERE NOT NULL >= ( NULL )
----

query I rowsort
SELECT - - col0 * col0 FROM tab2 AS cor0
----
49
6084
6241

query I rowsort
SELECT col0 + cor0.col1 AS col2 FROM tab0 AS cor0
----
110
132
180

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0, tab2 AS cor0
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT - - col1 * col0 + - col1 FROM tab0 AS cor0
----
1978
3298
8008

query I rowsort
SELECT 81 * col2 + col2 AS col1 FROM tab1 AS cor0
----
4428
4674
7872

query I rowsort
SELECT 60 * col0 FROM tab2
----
420
4680
4740

query I rowsort
SELECT tab0.col0 FROM tab0, tab2 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query I rowsort
SELECT distinct 86 FROM tab0 AS cor0
----
86

query I rowsort
SELECT - col1 * - tab2.col0 AS col0 FROM tab2
----
1343
217
4602

query IIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query I rowsort
SELECT - col0 + col0 FROM tab2
----
0
0
0

query I rowsort
SELECT col0 * tab1.col2 AS col1 FROM tab1 WHERE ( - col1 ) NOT IN ( - col0 )
----
162
3648
7680

query I rowsort
SELECT distinct col0 - - col1 * col2 FROM tab2
----
1612
725
844

query I rowsort
SELECT distinct - col0 + col0 FROM tab2
----
0

query I rowsort
SELECT ALL - col0 FROM tab1 WHERE NULL >= col0
----

query I rowsort
SELECT tab0.col2 * col1 * col1 AS col2 FROM tab0
----
244068
679042
9409

query I rowsort
SELECT distinct col1 * col2 FROM tab2
----
1534
646
837

query III rowsort
SELECT * FROM tab2 WHERE ( NULL ) < ( col1 )
----
9 values hashing to ad05b5942400d5e7a21b323b3da65a45

query I rowsort
SELECT distinct col1 FROM tab0
----
86
91
97

query I rowsort
SELECT tab0.col2 AS col0 FROM tab0
----
1
33
82

query I rowsort
SELECT col0 AS col2 FROM tab1
----
3
64
80

query III rowsort
SELECT distinct * FROM tab0 WHERE NOT col2 * - tab0.col0 > NULL
----

query I rowsort
SELECT ALL + col1 + col1 FROM tab2
----
118
34
62

query I rowsort
SELECT tab1.col0 AS col0 FROM tab1
----
3
64
80

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 cor0 CROSS JOIN tab0
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query III rowsort
SELECT * FROM tab0 WHERE NOT col0 NOT IN ( tab0.col2 * col2 + col2 + col1 )
----

query I rowsort
SELECT - col1 * - cor0.col1 FROM tab1 AS cor0
----
100
169
676

query IIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0 CROSS JOIN tab1
----
243 values hashing to 877a8dbac0e29b86e845fb64ed9d2242

query III rowsort
SELECT * FROM tab0 WHERE NULL = ( col0 + - col1 )
----

query III rowsort
SELECT * FROM tab1 WHERE NOT NULL > ( NULL )
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query I rowsort
SELECT ALL + col2 * col2 FROM tab1
----
2916
3249
9216

query I rowsort
SELECT tab1.col1 * col2 FROM tab1
----
1248
1404
570

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col0 col0 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT distinct col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT cor0.col2 FROM tab0, tab2 AS cor0
----
9 values hashing to 5911bac51441f4ff640b2a2b721ea8e3

query I rowsort
SELECT ALL - cor0.col0 * - col1 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT cor0.col2 AS col0 FROM tab1 cor0
----
54
57
96

query I rowsort
SELECT col1 AS col0 FROM tab0 cor0
----
86
91
97

query I rowsort
SELECT distinct 15 * col0 FROM tab2 AS cor0
----
105
1170
1185

query I rowsort
SELECT - - col1 * col2 AS col0 FROM tab1 AS cor0
----
1248
1404
570

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col0 col1 FROM tab1 AS cor0
----
3
64
80

query IIIIIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab1, tab0 cor1
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab0, tab1 AS cor1, tab0 AS cor2, tab1 cor3
----
3645 values hashing to 7a2f620d56640e95048dfa9a4cf93159

query I rowsort
SELECT tab1.col1 * col0 * col2 AS col2 FROM tab1
----
36480
4212
99840

query I rowsort
SELECT distinct col2 FROM tab1
----
54
57
96

query I rowsort
SELECT ALL + col1 - - 54 * cor0.col1 FROM tab0 AS cor0
----
4730
5005
5335

query I rowsort
SELECT distinct col0 AS col2 FROM tab0 AS cor0
----
24
35
89

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 cor0, tab2 AS cor1
----
243 values hashing to 5ac29bd6e3a9e69ed9c73ca7a34114f7

query I rowsort
SELECT 68 AS col1 FROM tab1 cor0
----
68

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 cor0, tab0, tab2 AS cor1
----
972 values hashing to 9600bdf5bac0caec3229e87170cc40b3

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0, tab0 cor1
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query I rowsort
SELECT 21 * col0 + col0 FROM tab2 AS cor0
----
154
1716
1738

query I rowsort
SELECT 75 + col0 FROM tab2 AS cor0
----
153
154
82

query I rowsort
SELECT col0 * cor0.col0 FROM tab2 AS cor0
----
49
6084
6241

query I rowsort
SELECT - - col1 FROM tab1 AS cor0
----
10
13
26

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0, tab0, tab1 AS cor1
----
972 values hashing to 5621675b1bd32b061d284d0444c76601

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0 CROSS JOIN tab1
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query I rowsort
SELECT col2 * 2 AS col2 FROM tab1 cor0
----
108
114
192

query I rowsort
SELECT - col1 * - 65 + col1 * - cor0.col1 AS col1 FROM tab1 cor0
----
1014
550
676

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 cor0, tab2 cor1
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT ALL + col0 * 83 FROM tab0
----
1992
2905
7387

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab0 AS cor0, tab0 AS cor1
----
972 values hashing to ea0f747588ddf5869ee18a5e22d9f237

query I rowsort
SELECT col1 * col2 AS col1 FROM tab1
----
1248
1404
570

query I rowsort
SELECT col0 AS col0 FROM tab1 AS cor0
----
3
64
80

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab0 AS cor1, tab1 AS cor2
----
972 values hashing to 88213a0de4c0a44aaefe8bbffbcaf44a

query I rowsort
SELECT - - col1 AS col2 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ALL - col0 * ( - col1 ) FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT col1 AS col1 FROM tab0 cor0
----
86
91
97

query I rowsort
SELECT ALL - ( - col1 ) AS col2 FROM tab0 AS cor0
----
86
91
97

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1, tab2 cor0
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query I rowsort
SELECT ALL - col0 + col0 FROM tab2
----
0
0
0

query I rowsort
SELECT ALL + col1 + cor0.col0 FROM tab2 AS cor0
----
137
38
96

query I rowsort
SELECT col2 FROM tab0 cor0
----
1
33
82

query I rowsort
SELECT - - col0 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT ALL + 6 + col1 FROM tab1
----
16
19
32

query I rowsort
SELECT col0 + col1 AS col0 FROM tab0
----
110
132
180

query I rowsort
SELECT distinct col0 + col1 AS col0 FROM tab1
----
29
74
93

query I rowsort
SELECT - col2 * - col0 FROM tab0
----
35
7298
792

query I rowsort
SELECT ALL + 26 FROM tab1 AS cor0
----
26

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col0 col2 FROM tab0 AS cor0
----
24
35
89

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct 45 * cor0.col0 col1 FROM tab2 AS cor0
----
315
3510
3555

query I rowsort
SELECT ALL + col0 * 91 AS col0 FROM tab0
----
2184
3185
8099

query I rowsort
SELECT 55 AS col0 FROM tab1 AS cor0
----
55

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col2 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ALL + col0 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT distinct - - col1 AS col1 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT ALL - - col2 AS col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT ALL + col0 * 71 AS col0 FROM tab2
----
497
5538
5609

query I rowsort
SELECT distinct cor0.col2 + col0 AS col1 FROM tab1 AS cor0
----
121
176
57

query I rowsort
SELECT distinct - col0 + col0 FROM tab2 AS cor0
----
0

query I rowsort
SELECT tab2.col0 FROM tab2, tab1 AS cor0, tab1 AS cor1
----
27 values hashing to 1e1f10953eb8effe9b20e746f8a7fd83

query I rowsort
SELECT ALL - - col2 AS col2 FROM tab1 cor0
----
54
57
96

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab1 AS cor0
----
243 values hashing to 70c6a01760d7239f3003db4da92180a4

query I rowsort
SELECT ( - col1 ) * - col1 FROM tab0
----
7396
8281
9409

query I rowsort
SELECT - 70 * - col2 FROM tab2 AS cor0
----
1820
1890
2660

query IIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab1 cor1
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query I rowsort
SELECT distinct 74 AS col0 FROM tab0
----
74

query I rowsort
SELECT 74 + - col2 AS col0 FROM tab2 AS cor0
----
36
47
48

query I rowsort
SELECT col2 * 70 FROM tab0
----
2310
5740
70

query I rowsort
SELECT - - col1 FROM tab0 cor0
----
86
91
97

query I rowsort
SELECT ALL + col0 + col0 AS col2 FROM tab2 AS cor0
----
14
156
158

query I rowsort
SELECT 55 FROM tab0 AS cor0
----
55

query I rowsort
SELECT col0 * col1 AS col2 FROM tab1 cor0
----
1040
640
78

query I rowsort
SELECT tab0.col1 AS col0 FROM tab0
----
86
91
97

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab0 cor0
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query I rowsort
SELECT ALL + 16 FROM tab1 AS cor0
----
16

query I rowsort
SELECT ALL - - 34 FROM tab1 AS cor0
----
34

query I rowsort
SELECT distinct 45 FROM tab1 AS cor0
----
45

query I rowsort
SELECT col0 AS col0 FROM tab1
----
3
64
80

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 cor0, tab1 AS cor1
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query I rowsort
SELECT ALL + 20 FROM tab0
----
20

query I rowsort
SELECT ALL + 41 FROM tab2
----
41

query I rowsort
SELECT ALL + 97 AS col1 FROM tab0
----
97

query I rowsort
SELECT cor0.col1 FROM tab2, tab2 AS cor0, tab1 AS cor1
----
27 values hashing to 7599b480125de521efed71b5b2413c7d

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 col1 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT - col2 * - cor0.col2 FROM tab2 AS cor0
----
1444
676
729

query I rowsort
SELECT col1 + ( col0 * - col1 ) AS col1 FROM tab0
----
4294959288
4294963998
4294965318

query I rowsort
SELECT col2 AS col0 FROM tab0
----
1
33
82

query I rowsort
SELECT distinct col2 AS col1 FROM tab1
----
54
57
96

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 + col1 col0 FROM tab2
----
55
58
85

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + cor0.col1 col1 FROM tab0 AS cor0
----
86
91
97

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col1 col0 FROM tab1
----
10
13
26

query I rowsort
SELECT cor0.col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT ALL - cor0.col0 * - col0 AS col1 FROM tab0 AS cor0
----
1225
576
7921

query I rowsort
SELECT ( cor0.col2 ) AS col0 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT ALL + - ( - 26 ) * col2 AS col0 FROM tab1 AS cor0
----
1404
1482
2496

query I rowsort
SELECT ALL - - 33 - - 38 AS col1 FROM tab0 AS cor0
----
71

query I rowsort
SELECT distinct cor0.col0 * col2 + - col1 FROM tab1 AS cor0
----
136
3638
7667

query I rowsort
SELECT ALL + col1 AS col1 FROM tab1 cor0
----
10
13
26

query I rowsort
SELECT ALL + 61 * col1 FROM tab1 AS cor0
----
1586
610
793

query I rowsort
SELECT tab2.col0 AS col2 FROM tab2, tab2 AS cor0
----
9 values hashing to 95b96ca1dbe2e39a0fa78f50d374f51a

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT tab2.col1 col0 FROM tab2
----
17
31
59

query I rowsort
SELECT ALL - - col2 + 32 AS col1 FROM tab0 AS cor0
----
114
33
65

query I rowsort
SELECT - - col2 + col0 FROM tab1 AS cor0
----
121
176
57

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0, tab1 AS cor1
----
243 values hashing to 2464a6f4cfabe66aeca50fcb4cd85bf5

query I rowsort
SELECT col2 - tab1.col1 FROM tab1
----
28
47
83

query IIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

query IIIIII rowsort
SELECT distinct * FROM tab1 cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query I rowsort
SELECT 36 AS col0 FROM tab0
----
36

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0, tab1 AS cor1
----
243 values hashing to 70c6a01760d7239f3003db4da92180a4

query I rowsort
SELECT ALL - 87 * cor0.col2 * - col2 FROM tab0 AS cor0
----
584988
87
94743

query I rowsort
SELECT col1 * col1 + - col2 FROM tab1 AS cor0
----
43
622
73

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 cor0, tab2 cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT col1 + - tab0.col1 FROM tab0
----
0
0
0

query I rowsort
SELECT distinct tab2.col0 + col0 AS col2 FROM tab2
----
14
156
158

query I rowsort
SELECT distinct col1 * col1 FROM tab1
----
100
169
676

query I rowsort
SELECT distinct tab2.col0 + col2 FROM tab2
----
104
117
34

query I rowsort
SELECT distinct col2 * col0 FROM tab2
----
189
2028
3002

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - col2 * - col0 col2 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT col1 + col0 AS col2 FROM tab0 cor0
----
110
132
180

query I rowsort
SELECT - - cor0.col0 AS col2 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT ALL - col2 * - col0 FROM tab2
----
189
2028
3002

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab2 cor0, tab2
----
972 values hashing to a698694a7dac245e42212ff0316bdf45

query I rowsort
SELECT distinct - col0 * - col2 AS col1 FROM tab1
----
162
3648
7680

query I rowsort
SELECT distinct col1 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT col1 * col1 FROM tab1 AS cor0
----
100
169
676

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab2, tab2 AS cor1
----
972 values hashing to 82def1c3361e635dd4cf447edc22edb9

query IIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab2 cor1
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0, tab2 cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT 68 * col0 FROM tab0
----
1632
2380
6052

query IIIIIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab1, tab2 cor1, tab2 AS cor2
----
972 values hashing to 64ce0e736818e884f0a9ecd075da5eb7

query IIIIIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab0, tab0 AS cor1
----
243 values hashing to 3e8bd9634a3f5947d8becd5f5799bb7f

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0, tab0 cor1, tab2 AS cor2
----
972 values hashing to 89714dd446b7a97f8787d5744bdbf323

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab2 cor1
----
243 values hashing to d489341cd587fd6eb0b972c5464c6ddc

query I rowsort
SELECT - - col1 AS col2 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT - 30 * - cor0.col1 + col1 FROM tab0 cor0
----
2666
2821
3007

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col1 FROM tab0 cor0
----
86
91
97

query I rowsort
SELECT distinct col1 AS col2 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT cor0.col0 AS col2 FROM tab1, tab0 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query I rowsort
SELECT - - col1 * col2 AS col0 FROM tab0 cor0
----
2838
7462
97

query I rowsort
SELECT ALL + col2 * cor0.col0 AS col2 FROM tab2 AS cor0
----
189
2028
3002

query IIIIIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab2, tab2 AS cor1
----
243 values hashing to 5ac29bd6e3a9e69ed9c73ca7a34114f7

query I rowsort
SELECT distinct 81 FROM tab1
----
81

query I rowsort
SELECT col2 * cor0.col0 FROM tab0 AS cor0
----
35
7298
792

query I rowsort
SELECT ALL + 37 AS col0 FROM tab0
----
37

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0, tab0 AS cor0
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

query I rowsort
SELECT cor0.col2 AS col0 FROM tab2, tab0 AS cor0
----
9 values hashing to c8f9fa9ef0f8702bd382e821378a96d8

query I rowsort
SELECT tab1.col2 AS col2 FROM tab1 AS cor0 CROSS JOIN tab1
----
9 values hashing to 80ca0a1cc337a7714a8990a764cfdb17

query IIIIII rowsort
SELECT * FROM tab2 cor0 CROSS JOIN tab2
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query I rowsort
SELECT distinct col1 AS col1 FROM tab0
----
86
91
97

query IIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab1
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 col2 FROM tab0
----
1
33
82

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab2
----
54 values hashing to d8165ceb99ded93f34ad83c310a80ea7

query I rowsort
SELECT ALL + col0 AS col0 FROM tab1
----
3
64
80

query I rowsort
SELECT ALL - tab0.col2 FROM tab0 WHERE ( col1 * - col1 ) < ( NULL )
----

query I rowsort
SELECT tab0.col1 FROM tab0
----
86
91
97

query III rowsort
SELECT * FROM tab0 WHERE NOT ( NULL ) > NULL
----

query I rowsort
SELECT col2 * col0 AS col1 FROM tab2 cor0
----
189
2028
3002

query I rowsort
SELECT col1 * col2 FROM tab1 AS cor0
----
1248
1404
570

query I rowsort
SELECT distinct col0 AS col2 FROM tab0
----
24
35
89

query I rowsort
SELECT distinct tab0.col2 + col1 + col2 FROM tab0
----
152
255
99

query I rowsort
SELECT distinct tab2.col2 * col2 + col2 AS col1 FROM tab2
----
1482
702
756

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 * col2 + col0 * col2 + - col0 * - col2 col2 FROM tab2
----
1107
4732
7448

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL - cor0.col2 * - col0 + - col0 col2 FROM tab2 AS cor0
----
182
1950
2923

query I rowsort
SELECT distinct col0 * col1 AS col0 FROM tab1 AS cor0
----
1040
640
78

query I rowsort
SELECT ALL + col2 AS col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT distinct col2 AS col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT distinct col1 * tab2.col0 + col0 AS col2 FROM tab2
----
1422
224
4680

query I rowsort
SELECT ALL + tab0.col0 FROM tab0
----
24
35
89

query I rowsort
SELECT distinct - ( - 57 ) AS col0 FROM tab1 AS cor0
----
57

query I rowsort
SELECT col0 * col1 FROM tab0 cor0
----
2064
3395
8099

query I rowsort
SELECT ALL - col0 * - col0 FROM tab2 AS cor0
----
49
6084
6241

query I rowsort
SELECT distinct cor0.col1 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT 35 * col0 AS col1 FROM tab0 AS cor0
----
1225
3115
840

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col2 col1 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT ALL - col1 * - col1 + 90 FROM tab1 AS cor0
----
190
259
766

query I rowsort
SELECT col1 * col1 AS col1 FROM tab1 AS cor0
----
100
169
676

query I rowsort
SELECT col0 + col1 AS col2 FROM tab2 AS cor0
----
137
38
96

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT cor0.col0 AS col1 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT distinct - col1 * col0 * - col1 AS col2 FROM tab0 AS cor0
----
177504
329315
737009

query I rowsort
SELECT - cor0.col2 * - col0 FROM tab2 AS cor0
----
189
2028
3002

query IIIIIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab1, tab1 AS cor1, tab2 AS cor2
----
972 values hashing to 72eb3d4d523f5d0c69d1b855edd18f4a

query I rowsort
SELECT col0 + 23 * col2 AS col0 FROM tab2 cor0
----
628
676
953

query I rowsort
SELECT distinct 70 FROM tab0
----
70

query IIIIII rowsort
SELECT * FROM tab2 cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query I rowsort
SELECT 9 FROM tab2
----
9

query I rowsort
SELECT distinct col2 * col1 AS col0 FROM tab2
----
1534
646
837

query I rowsort
SELECT ( col2 * col0 + - col1 ) AS col1 FROM tab1
----
136
3638
7667

query I rowsort
SELECT ( tab2.col1 ) FROM tab2
----
17
31
59

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab1 AS cor1, tab2 cor2
----
972 values hashing to 2507aa9f48c3db94de9fec065edf3731

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 cor0 CROSS JOIN tab0
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0 CROSS JOIN tab2
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab1, tab0 AS cor1
----
972 values hashing to b51b4342db121ebc2d3d353dcd8ed521

query I rowsort
SELECT - col2 + - col0 * - cor0.col2 AS col1 FROM tab1 AS cor0
----
108
3591
7584

query I rowsort
SELECT distinct - col1 - - col1 AS col1 FROM tab0 AS cor0
----
0

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 AS cor0, tab1 AS cor1, tab0 cor2
----
972 values hashing to b51b4342db121ebc2d3d353dcd8ed521

query I rowsort
SELECT ALL + 99 FROM tab0
----
99

query I rowsort
SELECT ALL + col1 FROM tab0 cor0
----
86
91
97

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 + cor0.col0 col0 FROM tab0 AS cor0
----
171
36
57

query I rowsort
SELECT distinct - - 90 + col0 AS col0 FROM tab1 AS cor0
----
154
170
93

query I rowsort
SELECT ALL + cor0.col0 AS col2 FROM tab0 AS cor0
----
24
35
89

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab1 AS cor0, tab1
----
972 values hashing to fe55095fff3a5ecc2f113d14a8c6f823

query I rowsort
SELECT distinct col1 AS col0 FROM tab2
----
17
31
59

query I rowsort
SELECT - col0 * - 35 FROM tab1
----
105
2240
2800

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab0 AS cor1, tab1 AS cor2
----
972 values hashing to 465d072d2d9eababbfc8e88b82707474

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0 cor0, tab1 AS cor1, tab0 AS cor2
----
972 values hashing to 5e655b1287771868a8f868574a94d749

query I rowsort
SELECT 36 FROM tab2 AS cor0
----
36

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT tab1.col2 col2 FROM tab1, tab0 AS cor0
----
9 values hashing to 80ca0a1cc337a7714a8990a764cfdb17

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 cor0, tab0 cor1
----
243 values hashing to 3a953203ced079e372111d61dbd9e35f

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col1 * - 7 + cor0.col1 * cor0.col0 * col1 col0 FROM tab2 AS cor0
----
22712
271105
6510

query I rowsort
SELECT ALL + cor0.col0 * 75 AS col2 FROM tab1 AS cor0
----
225
4800
6000

query I rowsort
SELECT col1 + col2 FROM tab0
----
119
173
98

query IIIIIIIIIIIIIIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab0, tab1 AS cor1, tab1, tab2 AS cor2, tab0 AS cor3
----
13122 values hashing to 76444691021e654ba468b5c8fca61882

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col0 + col0 col0 FROM tab1
----
128
160
6

query IIIIIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab0, tab1 AS cor1
----
243 values hashing to 9ed1a6a444254225f040123c46b7f70c

query I rowsort
SELECT ALL + col2 * col0 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT - - col0 * 26 + cor0.col2 FROM tab2 cor0
----
2054
209
2092

query I rowsort
SELECT col2 * 60 - 87 AS col0 FROM tab1 AS cor0
----
3153
3333
5673

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 cor0, tab0 AS cor1
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query I rowsort
SELECT tab0.col0 FROM tab0, tab0 cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query I rowsort
SELECT ALL + col0 FROM tab1
----
3
64
80

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 cor0, tab2 AS cor1
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT distinct - cor0.col0 * - col1 AS col0 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT - col0 + col0 AS col0 FROM tab2 cor0
----
0
0
0

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0, tab2 cor1
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT - - ( col1 ) + col1 FROM tab2 cor0
----
118
34
62

query I rowsort
SELECT 76 AS col0 FROM tab1
----
76

query I rowsort
SELECT 93 AS col1 FROM tab2
----
93

query I rowsort
SELECT ALL + col0 AS col0 FROM tab0
----
24
35
89

query I rowsort
SELECT col1 AS col2 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT - - col1 * col0 AS col0 FROM tab2 cor0
----
1343
217
4602

query I rowsort
SELECT - - col2 * col2 FROM tab1 AS cor0
----
2916
3249
9216

query I rowsort
SELECT cor0.col2 AS col0 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT 75 AS col2 FROM tab1
----
75

query I rowsort
SELECT distinct cor0.col0 + cor0.col1 AS col2 FROM tab2 AS cor0
----
137
38
96

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab2 AS cor1, tab1 AS cor2
----
972 values hashing to 4c0813b2179303fdf58f082d81d6d03c

query I rowsort
SELECT ALL + tab2.col1 FROM tab2, tab1 AS cor0
----
9 values hashing to c61d27a0022e6d022371dc58819ab272

query I rowsort
SELECT distinct col1 * col0 FROM tab1
----
1040
640
78

query I rowsort
SELECT col2 + tab2.col0 FROM tab2
----
104
117
34

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT tab0.col1 col2 FROM tab0
----
86
91
97

query I rowsort
SELECT distinct col2 + - col1 FROM tab1
----
28
47
83

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 col1 FROM tab0
----
1
33
82

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab0 AS cor0, tab0 cor1
----
243 values hashing to 3e8bd9634a3f5947d8becd5f5799bb7f

query I rowsort
SELECT col2 * col0 FROM tab0
----
35
7298
792

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 cor0, tab0, tab1 cor1
----
972 values hashing to 0210050fb1701e2797a9b17e1ebac91e

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 AS cor0, tab1, tab2 AS cor1
----
972 values hashing to 01a5931cccc3dad8792a1bc6df09c614

query I rowsort
SELECT 91 FROM tab2
----
91

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0 CROSS JOIN tab1 AS cor1
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query I rowsort
SELECT distinct cor0.col0 AS col0 FROM tab1, tab1 cor0 CROSS JOIN tab2, tab2 cor1, tab0 AS cor2
----
3
64
80

query I rowsort
SELECT ALL - 81 * - col1 AS col0 FROM tab1 cor0
----
1053
2106
810

query I rowsort
SELECT distinct col0 + cor0.col2 AS col2 FROM tab0 AS cor0
----
171
36
57

query I rowsort
SELECT - - 78 FROM tab0 AS cor0
----
78

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 cor0, tab1, tab1 AS cor1
----
972 values hashing to fe55095fff3a5ecc2f113d14a8c6f823

query I rowsort
SELECT ( col1 ) * 95 AS col1 FROM tab1
----
1235
2470
950

query I rowsort
SELECT distinct - 51 AS col1 FROM tab2 AS cor0
----
4294967245

query I rowsort
SELECT ALL + col1 AS col1 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ( - col1 ) + col1 AS col2 FROM tab1 AS cor0
----
0
0
0

query I rowsort
SELECT distinct col0 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT distinct - - col2 + col0 AS col1 FROM tab1 AS cor0
----
121
176
57

query I rowsort
SELECT distinct - col2 + col0 * col1 FROM tab0 AS cor0
----
2031
3394
8017

query I rowsort
SELECT - - col0 * col0 FROM tab0 cor0
----
1225
576
7921

query I rowsort
SELECT 60 FROM tab1
----
60

query I rowsort
SELECT distinct col0 AS col0 FROM tab0
----
24
35
89

query I rowsort
SELECT distinct cor1.col2 * 75 FROM tab1, tab1 AS cor0, tab1 AS cor1
----
4050
4275
7200

query I rowsort
SELECT distinct col1 AS col0 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT - - col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT 42 FROM tab0
----
42

query I rowsort
SELECT distinct 56 FROM tab2
----
56

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ( col2 + col2 ) col0 FROM tab0
----
164
2
66

query I rowsort
SELECT col2 + ( col1 ) FROM tab0 AS cor0
----
119
173
98

query I rowsort
SELECT col2 * col0 AS col2 FROM tab0 AS cor0
----
35
7298
792

query I rowsort
SELECT 40 FROM tab1 AS cor0
----
40

query I rowsort
SELECT distinct tab2.col2 AS col0 FROM tab2
----
26
27
38

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct tab0.col2 col2 FROM tab0
----
1
33
82

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 + col2 * - col0 * - col0 col1 FROM tab2 AS cor0
----
1354
158243
237175

query I rowsort
SELECT ALL - - col0 + col0 * col2 FROM tab1 AS cor0
----
165
3712
7760

query I rowsort
SELECT - 84 * - col1 FROM tab1 AS cor0
----
1092
2184
840

query IIIIII rowsort
SELECT * FROM tab1 cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to 341cdc053c309cf3abe57fa060ecf96e

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col0 * col2 col0 FROM tab1
----
162
3648
7680

query I rowsort
SELECT col2 + col0 AS col2 FROM tab2 cor0
----
104
117
34

query I rowsort
SELECT ALL + col0 AS col1 FROM tab0 cor0
----
24
35
89

query I rowsort
SELECT ALL + col0 AS col1 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT 17 + col1 AS col0 FROM tab1
----
27
30
43

query I rowsort
SELECT 46 FROM tab1
----
46

query IIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab0, tab2 cor1
----
243 values hashing to ce53c0e8839c969b0513568da6eb2c4b

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col0 FROM tab2
----
17
31
59

query I rowsort
SELECT ( col1 ) AS col0 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT - - col1 + col1 AS col1 FROM tab0 cor0
----
172
182
194

query I rowsort
SELECT 8 AS col1 FROM tab0 AS cor0
----
8

query I rowsort
SELECT ALL + cor0.col1 * col1 * col2 - - col2 * col0 AS col0 FROM tab0 AS cor0
----
244860
686340
9444

query I rowsort
SELECT cor0.col0 * cor0.col0 * cor0.col2 FROM tab0 AS cor0
----
1225
19008
649522

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - - col0 + col1 col0 FROM tab0 AS cor0
----
110
132
180

query I rowsort
SELECT distinct - - col0 * col1 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT distinct 97 FROM tab1 AS cor0
----
97

query I rowsort
SELECT - - 54 FROM tab0 AS cor0
----
54

query I rowsort
SELECT 94 * col0 FROM tab0
----
2256
3290
8366

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab1 AS cor1, tab2, tab2 AS cor2
----
3645 values hashing to 803a5565701c4ced6bba69940782c17a

query I rowsort
SELECT tab0.col1 AS col0 FROM tab0, tab2 AS cor0
----
9 values hashing to 585a41a52c0c6c0d697b5d39265b74dc

query I rowsort
SELECT ALL - col1 + 89 AS col2 FROM tab1 AS cor0
----
63
76
79

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col1 col1 FROM tab1
----
10
13
26

query I rowsort
SELECT - col0 + 97 FROM tab0
----
62
73
8

query I rowsort
SELECT tab0.col2 FROM tab0, tab0 cor0, tab2 AS cor1
----
27 values hashing to 7786718bd8042022537378d40ec87475

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 cor0, tab2 AS cor1
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query I rowsort
SELECT col2 + - col2 AS col0 FROM tab0
----
0
0
0

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + cor0.col2 col0 FROM tab1, tab2 AS cor0
----
9 values hashing to 5911bac51441f4ff640b2a2b721ea8e3

query I rowsort
SELECT distinct col2 + col2 AS col1 FROM tab0 AS cor0
----
164
2
66

query I rowsort
SELECT ALL - - col2 FROM tab0 AS cor0
----
1
33
82

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 AS cor0, tab0 AS cor1, tab0 AS cor2
----
972 values hashing to 8420206d6932c454f05a38de634b3cb5

query I rowsort
SELECT distinct col1 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT col1 AS col2 FROM tab2 AS cor0
----
17
31
59

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col2 col0 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT - - col1 AS col2 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT ALL + tab0.col2 AS col2 FROM tab0
----
1
33
82

query I rowsort
SELECT col0 + 22 FROM tab1 AS cor0
----
102
25
86

query I rowsort
SELECT col0 * col1 FROM tab0
----
2064
3395
8099

query I rowsort
SELECT 38 FROM tab0 cor0
----
38

query I rowsort
SELECT col2 * - col1 * - col0 FROM tab0
----
3395
664118
68112

query I rowsort
SELECT cor0.col1 AS col2 FROM tab2, tab1 AS cor0, tab1 AS cor1
----
27 values hashing to d671a064e2da709ca4cdfea317b8e892

query I rowsort
SELECT 33 AS col2 FROM tab1 AS cor0
----
33

query I rowsort
SELECT 35 + cor0.col1 FROM tab1 AS cor0
----
45
48
61

query I rowsort
SELECT - - col1 * cor0.col2 + ( 73 * col2 ) FROM tab2 AS cor0
----
2808
3420
3432

query I rowsort
SELECT distinct tab0.col0 FROM tab0, tab2, tab2 cor0
----
24
35
89

query I rowsort
SELECT - ( 36 ) * - col0 FROM tab0
----
1260
3204
864

query I rowsort
SELECT distinct 14 + 16 FROM tab1
----
30

query I rowsort
SELECT ALL + col0 + col0 FROM tab1 AS cor0
----
128
160
6

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 cor0, tab2 cor1
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0, tab0 AS cor1, tab2 AS cor2
----
972 values hashing to 591a9a93560839231c038a1e10bd240a

query I rowsort
SELECT 77 - - col0 FROM tab1
----
141
157
80

query I rowsort
SELECT - col0 * - tab1.col2 FROM tab1
----
162
3648
7680

query I rowsort
SELECT col2 AS col1 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT distinct col1 * col2 AS col2 FROM tab0 AS cor0
----
2838
7462
97

query I rowsort
SELECT distinct col0 * 63 FROM tab0
----
1512
2205
5607

query I rowsort
SELECT distinct col2 AS col2 FROM tab2
----
26
27
38

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0 CROSS JOIN tab0
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0 CROSS JOIN tab2, tab1 AS cor1, tab2 AS cor2
----
3645 values hashing to 6193516da5556fc054f35e0d2f4e5372

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab1, tab1 AS cor1
----
972 values hashing to 635619591835474e6aa6acdff4ab166c

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 cor0, tab1 AS cor1
----
243 values hashing to 2464a6f4cfabe66aeca50fcb4cd85bf5

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 AS cor0, tab2 cor1
----
243 values hashing to 5ac29bd6e3a9e69ed9c73ca7a34114f7

query I rowsort
SELECT cor0.col2 AS col0 FROM tab0 AS cor0
----
1
33
82

query IIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab1 cor1
----
243 values hashing to 877a8dbac0e29b86e845fb64ed9d2242

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL - - col0 + col0 col2 FROM tab0 AS cor0
----
178
48
70

query I rowsort
SELECT ALL - col1 * - col1 * col1 AS col2 FROM tab2 AS cor0
----
205379
29791
4913

query I rowsort
SELECT ( col2 ) + - col1 + col1 * col0 FROM tab2 AS cor0
----
1364
213
4569

query I rowsort
SELECT - col0 + col0 * col1 * tab2.col1 AS col2 FROM tab2
----
22752
271440
6720

query I rowsort
SELECT 88 + col0 AS col2 FROM tab1 AS cor0
----
152
168
91

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab0 AS cor1, tab2, tab2 AS cor2
----
3645 values hashing to 17ceecc141378b185d60a17e53464c26

query I rowsort
SELECT ALL + col2 * cor0.col0 - ( - col2 ) AS col2 FROM tab0 AS cor0
----
36
7380
825

query I rowsort
SELECT ALL - - col1 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT ALL - - col1 AS col1 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT ALL + col2 * col1 FROM tab1 AS cor0
----
1248
1404
570

query I rowsort
SELECT col2 * 56 FROM tab1 AS cor0
----
3024
3192
5376

query I rowsort
SELECT ALL + cor0.col1 FROM tab1 AS cor0
----
10
13
26

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ( col2 ) + col1 col0 FROM tab0 cor0
----
119
173
98

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 AS cor0 CROSS JOIN tab2, tab2 AS cor1
----
972 values hashing to f9adf26f20dc8fcc43c2de18a5fd4859

query IIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab1 cor1
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query I rowsort
SELECT ALL + col0 FROM tab2
----
7
78
79

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 cor0, tab1 cor1
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query I rowsort
SELECT tab2.col2 FROM tab2
----
26
27
38

query I rowsort
SELECT 22 * col1 AS col0 FROM tab0
----
1892
2002
2134

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - col1 + col1 col2 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT cor1.col1 FROM tab2, tab1 AS cor0, tab0 AS cor1, tab1 AS cor2
----
81 values hashing to 8c9db501a604ea66e3b5e5598f3f2a91

query I rowsort
SELECT col1 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT distinct tab0.col1 FROM tab0
----
86
91
97

query I rowsort
SELECT distinct - cor0.col2 * - col1 * ( col1 ) + - 68 AS col0 FROM tab0 cor0
----
244000
678974
9341

query I rowsort
SELECT col2 AS col0 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT distinct - ( - cor0.col0 ) - col1 AS col2 FROM tab1 AS cor0
----
4294967273
54
67

query I rowsort
SELECT - 0 AS col1 FROM tab1 AS cor0
----
0

query I rowsort
SELECT 49 * col1 AS col1 FROM tab1 AS cor0
----
1274
490
637

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 col2 FROM tab1
----
3
64
80

query I rowsort
SELECT ALL + ( col2 * col2 ) FROM tab2
----
1444
676
729

query I rowsort
SELECT - - 6 FROM tab0 AS cor0
----
6

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab2 AS cor1, tab1, tab1 AS cor2
----
3645 values hashing to 199388980dc5177ebebcfdbc0408ba02

query I rowsort
SELECT distinct - col1 + ( col1 ) FROM tab0 cor0
----
0

query IIIIII rowsort
SELECT * FROM tab2 cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query IIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab2 cor1
----
243 values hashing to 5ac29bd6e3a9e69ed9c73ca7a34114f7

query I rowsort
SELECT ALL + col2 AS col2 FROM tab2
----
26
27
38

query I rowsort
SELECT cor0.col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT ALL + ( col2 ) * tab2.col1 * col2 AS col0 FROM tab2
----
22599
24548
39884

query I rowsort
SELECT ALL + col2 * cor0.col1 + - col2 AS col2 FROM tab0 AS cor0
----
2805
7380
96

query I rowsort
SELECT ALL - 69 + col1 FROM tab0 AS cor0
----
17
22
28

query I rowsort
SELECT distinct 36 * col2 FROM tab2
----
1368
936
972

query I rowsort
SELECT col1 * cor0.col0 AS col0 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT ALL + cor0.col1 + - col2 FROM tab0 cor0
----
53
9
96

query I rowsort
SELECT ALL + col1 * cor0.col0 FROM tab1 AS cor0
----
1040
640
78

query IIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab2, tab2 cor1
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

query I rowsort
SELECT col2 + 60 AS col0 FROM tab1 AS cor0
----
114
117
156

query I rowsort
SELECT col2 + 7 AS col2 FROM tab1 AS cor0
----
103
61
64

query I rowsort
SELECT ALL - ( - 17 ) * cor0.col1 FROM tab0 AS cor0
----
1462
1547
1649

query I rowsort
SELECT - - 64 FROM tab2 AS cor0
----
64

query I rowsort
SELECT distinct col1 + 66 FROM tab2 AS cor0
----
125
83
97

query I rowsort
SELECT col1 + col0 AS col0 FROM tab1 AS cor0
----
29
74
93

query I rowsort
SELECT distinct 43 FROM tab0
----
43

query I rowsort
SELECT 81 + col2 * col0 + col0 FROM tab2 AS cor0
----
2187
277
3162

query I rowsort
SELECT distinct 30 FROM tab1 cor0
----
30

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0 CROSS JOIN tab1, tab1 cor1
----
972 values hashing to f8fe28681e8720551e1ec173631fc529

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab0 AS cor1, tab1 AS cor2
----
972 values hashing to 2d99dda76af061a3fac120e0e49e6c53

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2 cor0, tab1, tab2 AS cor1
----
972 values hashing to bcf430f79386b43bc4077271fcd15cf0

query I rowsort
SELECT ALL + cor0.col0 FROM tab2, tab0 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query I rowsort
SELECT cor0.col0 AS col0 FROM tab1 AS cor0 CROSS JOIN tab1 AS cor1
----
9 values hashing to dd18b93263a6cd425fc7cc84d9137870

query I rowsort
SELECT col1 * 22 FROM tab1 cor0
----
220
286
572

query I rowsort
SELECT ALL + col2 + col1 FROM tab0 AS cor0
----
119
173
98

query I rowsort
SELECT col2 * ( col0 ) AS col2 FROM tab0 AS cor0
----
35
7298
792

query I rowsort
SELECT ALL + col2 + col1 AS col2 FROM tab1
----
109
67
80

query I rowsort
SELECT col1 + col1 AS col2 FROM tab0
----
172
182
194

query I rowsort
SELECT ALL + col1 + col1 FROM tab0
----
172
182
194

query I rowsort
SELECT - cor0.col1 * - col0 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT - - col0 + col0 FROM tab1 AS cor0
----
128
160
6

query I rowsort
SELECT 22 AS col1 FROM tab2
----
22

query IIIIII rowsort
SELECT distinct * FROM tab2 cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query I rowsort
SELECT ALL - - col1 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT col1 * 36 AS col1 FROM tab1
----
360
468
936

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 cor0, tab2 cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT - col0 * ( - col2 ) FROM tab1
----
162
3648
7680

query IIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query I rowsort
SELECT col2 * 72 AS col2 FROM tab2
----
1872
1944
2736

query I rowsort
SELECT distinct ( col0 ) AS col1 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT col1 + 17 AS col0 FROM tab2
----
34
48
76

query I rowsort
SELECT distinct - cor0.col0 * - 69 FROM tab2, tab0 cor0
----
1656
2415
6141

query I rowsort
SELECT ALL + col2 AS col2 FROM tab0
----
1
33
82

query I rowsort
SELECT - - col0 * col2 + - col2 * - cor0.col1 FROM tab0 cor0
----
132
14760
3630

query I rowsort
SELECT - col2 * - 24 FROM tab1 AS cor0
----
1296
1368
2304

query I rowsort
SELECT col0 + - cor0.col0 FROM tab1 AS cor0
----
0
0
0

query I rowsort
SELECT distinct cor0.col1 AS col0 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT ALL + col0 * cor0.col2 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT col1 + ( col1 ) AS col1 FROM tab0 AS cor0
----
172
182
194

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 + col2 col0 FROM tab1
----
108
114
192

query I rowsort
SELECT ( - ( - col1 ) ) AS col0 FROM tab2
----
17
31
59

query IIIIII rowsort
SELECT distinct * FROM tab2 cor0 CROSS JOIN tab2 cor1
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - - col1 col2 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT 23 * cor0.col2 + - col2 AS col2 FROM tab2 AS cor0
----
572
594
836

query I rowsort
SELECT col0 * col1 AS col2 FROM tab2 AS cor0
----
1343
217
4602

query I rowsort
SELECT distinct col0 AS col1 FROM tab2 cor0
----
7
78
79

query I rowsort
SELECT - 48 * - col2 FROM tab0
----
1584
3936
48

query I rowsort
SELECT col2 * - col2 * - col1 AS col0 FROM tab1
----
119808
32490
75816

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1, tab1 cor0
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query I rowsort
SELECT distinct 64 * cor1.col1 AS col2 FROM tab1, tab1 AS cor0, tab0 AS cor1
----
5504
5824
6208

query I rowsort
SELECT 42 AS col2 FROM tab1
----
42

query I rowsort
SELECT ALL + 25 AS col1 FROM tab0 AS cor0
----
25

query I rowsort
SELECT distinct 83 * col1 AS col1 FROM tab2 AS cor0
----
1411
2573
4897

query I rowsort
SELECT ALL - - col1 + cor0.col1 FROM tab0 AS cor0
----
172
182
194

query I rowsort
SELECT - cor0.col0 * - col0 + col1 * 72 AS col0 FROM tab0 cor0
----
14473
6768
8209

query I rowsort
SELECT col0 + col2 FROM tab0
----
171
36
57

query I rowsort
SELECT ALL - col0 AS col1 FROM tab0 WHERE NOT NULL <> ( NULL )
----
4294967207
4294967261
4294967272

query I rowsort
SELECT ALL + col0 AS col2 FROM tab0
----
24
35
89

query I rowsort
SELECT distinct tab2.col1 AS col2 FROM tab2
----
17
31
59

query I rowsort
SELECT ALL + col0 * tab2.col2 FROM tab2
----
189
2028
3002

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT tab0.col1 * col1 col1 FROM tab0
----
7396
8281
9409

query I rowsort
SELECT col1 * col0 FROM tab1
----
1040
640
78

query I rowsort
SELECT 42 FROM tab1 AS cor0
----
42

query I rowsort
SELECT col1 AS col1 FROM tab1
----
10
13
26

query I rowsort
SELECT distinct col1 * col1 + - tab1.col2 AS col2 FROM tab1
----
43
622
73

query I rowsort
SELECT distinct col1 * - col1 AS col2 FROM tab0 WHERE - col1 >= ( NULL )
----
4294957887
4294959015
4294959900

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col0 FROM tab0
----
86
91
97

query I rowsort
SELECT col1 + col2 AS col1 FROM tab1 AS cor0
----
109
67
80

query I rowsort
SELECT col1 - col2 FROM tab0 AS cor0
----
53
9
96

query I rowsort
SELECT col1 FROM tab1 cor0
----
10
13
26

query I rowsort
SELECT ALL + col0 - col0 * - cor0.col1 FROM tab2 AS cor0
----
1422
224
4680

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 * tab0.col1 col2 FROM tab0
----
2838
7462
97

query I rowsort
SELECT distinct col1 + - col1 * - col0 AS col0 FROM tab0
----
2150
3492
8190

query I rowsort
SELECT tab0.col1 * col0 + col1 * col0 FROM tab0
----
16198
4128
6790

query I rowsort
SELECT ALL - col2 + col2 AS col1 FROM tab0
----
0
0
0

query I rowsort
SELECT ALL - ( - 94 ) * col0 AS col1 FROM tab1 AS cor0
----
282
6016
7520

query I rowsort
SELECT col1 * ( col1 ) AS col1 FROM tab1
----
100
169
676

query I rowsort
SELECT - 0 FROM tab1
----
0

query I rowsort
SELECT distinct col0 + 76 AS col0 FROM tab0
----
100
111
165

query I rowsort
SELECT distinct col2 * col0 AS col2 FROM tab2 cor0
----
189
2028
3002

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab1 cor0, tab2
----
972 values hashing to 0fcd8d0934383dd58863be894b07a6ed

query I rowsort
SELECT col2 + col0 - - col2 * col1 FROM tab1 AS cor0
----
1424
1461
691

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab2, tab2 AS cor1, tab0 AS cor2
----
972 values hashing to 63ccb67e72ebac679a0221202c067b9e

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col2 col2 FROM tab0 AS cor0
----
1
33
82

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab0 AS cor0, tab2 AS cor1
----
243 values hashing to ce53c0e8839c969b0513568da6eb2c4b

query I rowsort
SELECT distinct col1 + col2 FROM tab2 cor0
----
55
58
85

query I rowsort
SELECT distinct - ( - tab1.col2 ) + col0 FROM tab1
----
121
176
57

query I rowsort
SELECT col2 + 88 AS col0 FROM tab0
----
121
170
89

query I rowsort
SELECT - col0 * - col2 AS col1 FROM tab0 AS cor0
----
35
7298
792

query I rowsort
SELECT ALL - - col0 + col0 FROM tab2 AS cor0
----
14
156
158

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab1 AS cor0, tab0
----
972 values hashing to 9b91cf9fcc064ee1c13074a678b72ac7

query IIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab2, tab2 cor1
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query I rowsort
SELECT distinct - col2 * - col2 FROM tab2
----
1444
676
729

query I rowsort
SELECT - - col0 * cor0.col2 AS col2 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT ALL - col2 * - col0 FROM tab1
----
162
3648
7680

query I rowsort
SELECT ALL - - col1 * col0 AS col2 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT distinct - col0 * - col2 AS col0 FROM tab0
----
35
7298
792

query I rowsort
SELECT distinct cor0.col1 - - col2 FROM tab0 AS cor0
----
119
173
98

query I rowsort
SELECT ALL - - cor0.col2 * col1 FROM tab1 AS cor0
----
1248
1404
570

query I rowsort
SELECT ALL + - col0 + col0 * col2 FROM tab2 AS cor0
----
182
1950
2923

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT cor0.col2 col0 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT distinct cor0.col1 AS col0 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT ALL + col2 FROM tab1 cor0
----
54
57
96

query I rowsort
SELECT col0 * col2 FROM tab0 AS cor0
----
35
7298
792

query I rowsort
SELECT - col0 * - col0 FROM tab2 cor0
----
49
6084
6241

query I rowsort
SELECT distinct - - col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT cor0.col0 AS col0 FROM tab2, tab1 AS cor0, tab2 AS cor1
----
27 values hashing to 778b50575a9b91448119ee0ee1a9c44f

query I rowsort
SELECT ( 47 ) FROM tab0
----
47

query I rowsort
SELECT col2 * col2 FROM tab2 AS cor0
----
1444
676
729

query I rowsort
SELECT ALL + col1 * cor0.col2 + col0 AS col1 FROM tab2 cor0
----
1612
725
844

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0, tab0 cor1, tab1 AS cor2
----
972 values hashing to 82e15d5967b272804e574774895a0222

query I rowsort
SELECT distinct cor0.col1 AS col1 FROM tab1 AS cor0
----
10
13
26

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab2 AS cor1, tab1 AS cor2
----
972 values hashing to 92235dbc382d83baa93d6546ed489b0c

query I rowsort
SELECT ALL + col1 AS col2 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ALL - col2 * - cor0.col2 + - ( col0 ) FROM tab1 AS cor0
----
2913
3185
9136

query I rowsort
SELECT distinct cor0.col1 * 92 AS col1 FROM tab2 AS cor0 CROSS JOIN tab2 cor1
----
1564
2852
5428

query I rowsort
SELECT distinct col2 - - col0 FROM tab0 AS cor0
----
171
36
57

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 cor0, tab2 AS cor1
----
243 values hashing to 6506b295d3a7bcc5ed65956f5b4e38b0

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 cor0, tab0 cor1
----
243 values hashing to 3a953203ced079e372111d61dbd9e35f

query I rowsort
SELECT - col0 * col1 * - col2 FROM tab0
----
3395
664118
68112

query I rowsort
SELECT col1 * cor0.col2 FROM tab2 AS cor0
----
1534
646
837

query I rowsort
SELECT ALL - col2 * - col1 FROM tab1 AS cor0
----
1248
1404
570

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 col0 FROM tab0
----
1
33
82

query I rowsort
SELECT distinct 5 FROM tab1
----
5

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab0 AS cor0, tab2
----
972 values hashing to a9068b700464993db9fae6f630605fde

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab1 AS cor0, tab2 cor1
----
972 values hashing to f0b9665afa0b835e4e5097af17c51766

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0, tab1 cor1
----
243 values hashing to 70c6a01760d7239f3003db4da92180a4

query IIIIIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab2, tab1 AS cor1
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query I rowsort
SELECT - - cor0.col0 FROM tab1 AS cor0 CROSS JOIN tab1 AS cor1
----
9 values hashing to dd18b93263a6cd425fc7cc84d9137870

query I rowsort
SELECT ALL - - cor0.col2 * col2 FROM tab2 AS cor0
----
1444
676
729

query I rowsort
SELECT cor0.col0 FROM tab0, tab0 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 cor0, tab2 AS cor1
----
243 values hashing to d489341cd587fd6eb0b972c5464c6ddc

query I rowsort
SELECT ALL - - col1 AS col0 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT distinct col2 + 97 * 52 FROM tab0 AS cor0
----
5045
5077
5126

query I rowsort
SELECT - - col2 AS col2 FROM tab1 AS cor0
----
54
57
96

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2, tab1 AS cor0
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query I rowsort
SELECT col2 * col0 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT col0 AS col1 FROM tab0 AS cor0
----
24
35
89

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 AS cor0, tab0 cor1
----
243 values hashing to 74e36edda45186a5c45856859d8e21f0

query I rowsort
SELECT ALL + col2 + - col2 AS col2 FROM tab2
----
0
0
0

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1, tab1 AS cor0, tab0
----
972 values hashing to 909b7ebab62aff8f69dc42ccbb5c2eae

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab2 AS cor0, tab0
----
972 values hashing to e4c748f267e8d2a0e6d563281e1fb975

query I rowsort
SELECT distinct col2 * col1 FROM tab2
----
1534
646
837

query I rowsort
SELECT ALL + 75 FROM tab2 AS cor0
----
75

query I rowsort
SELECT col1 - cor0.col1 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT distinct col1 AS col2 FROM tab0
----
86
91
97

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col0 col2 FROM tab0
----
24
35
89

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1 cor0, tab1, tab0 AS cor1
----
972 values hashing to 909b7ebab62aff8f69dc42ccbb5c2eae

query I rowsort
SELECT ALL + col1 * cor0.col0 FROM tab1 cor0
----
1040
640
78

query I rowsort
SELECT tab2.col0 AS col0 FROM tab2
----
7
78
79

query I rowsort
SELECT - - col0 * col2 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT col2 * col2 FROM tab0 AS cor0
----
1
1089
6724

query I rowsort
SELECT distinct - 58 * - tab0.col0 FROM tab0
----
1392
2030
5162

query I rowsort
SELECT distinct col0 * 74 AS col0 FROM tab0 AS cor0
----
1776
2590
6586

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0, tab0 AS cor1, tab1 AS cor2
----
972 values hashing to 9af67d6f98010464af5d560bf949d487

query I rowsort
SELECT col2 AS col2 FROM tab0
----
1
33
82

query I rowsort
SELECT - ( - col2 ) FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT cor0.col1 + - col1 FROM tab2 AS cor0
----
0
0
0

query I rowsort
SELECT col2 AS col2 FROM tab2 AS cor0
----
26
27
38

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab0 AS cor0, tab1 AS cor1, tab0 AS cor2
----
972 values hashing to 5342fb4caf4767cb98bd21989bad099f

query I rowsort
SELECT cor0.col1 FROM tab0, tab0 AS cor0, tab2 AS cor1
----
27 values hashing to 2d6d3031dfe90e0c02db13aa63993bfd

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 AS cor0, tab2 AS cor1
----
243 values hashing to 5ac29bd6e3a9e69ed9c73ca7a34114f7

query I rowsort
SELECT distinct - col1 + cor0.col1 FROM tab0 AS cor0
----
0

query I rowsort
SELECT ALL + ( col0 ) AS col0 FROM tab1
----
3
64
80

query I rowsort
SELECT col2 * 91 FROM tab2 AS cor0
----
2366
2457
3458

query I rowsort
SELECT ALL - - col0 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT distinct cor0.col0 AS col0 FROM tab1, tab2, tab0 AS cor0
----
24
35
89

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1, tab2 cor0, tab0 AS cor1
----
972 values hashing to 58757c5bbbd4217c03cf2ac0b6126e55

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 cor0, tab1 AS cor1
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 cor0, tab1 AS cor1
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query I rowsort
SELECT cor0.col0 AS col0 FROM tab1, tab2 AS cor0, tab0 cor1
----
27 values hashing to 1e1f10953eb8effe9b20e746f8a7fd83

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 col1 FROM tab1
----
54
57
96

query I rowsort
SELECT distinct 34 AS col0 FROM tab0
----
34

query I rowsort
SELECT distinct 76 FROM tab1
----
76

query I rowsort
SELECT col0 * col1 FROM tab2 AS cor0
----
1343
217
4602

query I rowsort
SELECT ALL + 85 + - col2 + 76 FROM tab2 cor0
----
123
134
135

query I rowsort
SELECT - col1 + col1 + - col0 * - col0 AS col0 FROM tab1
----
4096
6400
9

query I rowsort
SELECT distinct - - col1 + cor0.col0 FROM tab1 cor0
----
29
74
93

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0, tab0 cor1
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query I rowsort
SELECT col1 * col0 AS col1 FROM tab2
----
1343
217
4602

query I rowsort
SELECT distinct - - cor0.col2 * col0 AS col0 FROM tab1 AS cor0
----
162
3648
7680

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab2, tab0 AS cor1
----
972 values hashing to 95de14c88adc44eda4adb5267fe9ebd1

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - - cor0.col2 * cor1.col2 col2 FROM tab1 AS cor0 CROSS JOIN tab1 AS cor1
----
9 values hashing to ede9f33694b1d188a31631cf33240c69

query I rowsort
SELECT distinct - ( 7 ) + cor0.col1 FROM tab2 AS cor0
----
10
24
52

query I rowsort
SELECT - col0 * - col0 FROM tab1 cor0
----
4096
6400
9

query I rowsort
SELECT distinct - cor0.col1 + col1 AS col2 FROM tab1 AS cor0
----
0

query I rowsort
SELECT distinct tab1.col2 FROM tab1
----
54
57
96

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col0 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ALL - - col2 AS col1 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT col1 - 24 AS col1 FROM tab0 AS cor0
----
62
67
73

query I rowsort
SELECT distinct col1 + col0 AS col1 FROM tab2 cor0
----
137
38
96

query I rowsort
SELECT ALL - - col1 * 58 - col1 FROM tab0 AS cor0
----
4902
5187
5529

query I rowsort
SELECT - - col0 * - ( - cor0.col1 ) + - col1 FROM tab1 AS cor0
----
1027
52
630

query I rowsort
SELECT - - cor0.col2 FROM tab0 AS cor0
----
1
33
82

query IIIIIIIII rowsort
SELECT distinct * FROM tab1 AS cor0 CROSS JOIN tab2, tab1 AS cor1
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query I rowsort
SELECT col2 AS col1 FROM tab1 cor0
----
54
57
96

query I rowsort
SELECT col0 * col2 AS col2 FROM tab1
----
162
3648
7680

query I rowsort
SELECT cor0.col0 * col1 AS col0 FROM tab1 AS cor0
----
1040
640
78

query I rowsort
SELECT ALL + col2 * col1 AS col1 FROM tab0
----
2838
7462
97

query I rowsort
SELECT col2 * col2 AS col0 FROM tab2
----
1444
676
729

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col2 FROM tab0
----
86
91
97

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col2 FROM tab2
----
17
31
59

query I rowsort
SELECT col1 + - col0 AS col0 FROM tab0
----
2
62
62

query I rowsort
SELECT cor0.col1 * col0 AS col0 FROM tab0 AS cor0
----
2064
3395
8099

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col0 col1 FROM tab0 cor0
----
24
35
89

query I rowsort
SELECT ALL + tab0.col2 FROM tab0
----
1
33
82

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab0
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query I rowsort
SELECT ALL + col2 AS col1 FROM tab1
----
54
57
96

query I rowsort
SELECT ALL + cor0.col0 + 23 FROM tab0 AS cor0
----
112
47
58

query I rowsort
SELECT distinct col0 * col0 + col1 AS col0 FROM tab1 AS cor0
----
35
4106
6413

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col2 * col0 + - cor0.col2 col0 FROM tab0 AS cor0
----
34
7216
759

query I rowsort
SELECT col0 - - tab0.col0 AS col0 FROM tab0
----
178
48
70

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2, tab1 AS cor0, tab0
----
972 values hashing to 9b91cf9fcc064ee1c13074a678b72ac7

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab1 AS cor0, tab0 AS cor1
----
972 values hashing to 95920403df268a272c4e933cd0bbe0be

query IIIIIIIII rowsort
SELECT * FROM tab1 cor0 CROSS JOIN tab1, tab2 AS cor1
----
243 values hashing to d489341cd587fd6eb0b972c5464c6ddc

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1 AS cor0 CROSS JOIN tab0, tab0 AS cor1, tab0 AS cor2
----
972 values hashing to 3406497351e4789c89a295ee9b64b201

query I rowsort
SELECT - col2 + ( cor0.col2 ) FROM tab0 AS cor0
----
0
0
0

query IIIIIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab0, tab0 AS cor1
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

query I rowsort
SELECT col0 * col1 * col1 FROM tab1
----
13520
2028
6400

query I rowsort
SELECT ALL + tab2.col1 FROM tab2
----
17
31
59

query I rowsort
SELECT col0 + col0 FROM tab0
----
178
48
70

query I rowsort
SELECT distinct col2 + - col1 + tab1.col1 AS col1 FROM tab1
----
54
57
96

query I rowsort
SELECT col2 * col2 AS col0 FROM tab1
----
2916
3249
9216

query I rowsort
SELECT col0 * - col1 * - col2 FROM tab2
----
119652
51034
5859

query I rowsort
SELECT - 24 * - col2 AS col1 FROM tab2
----
624
648
912

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 cor0, tab2 AS cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT col2 - col1 * - col2 FROM tab0 cor0
----
2871
7544
98

query I rowsort
SELECT distinct 29 AS col2 FROM tab2 AS cor0
----
29

query I rowsort
SELECT cor0.col2 + col1 FROM tab0 AS cor0
----
119
173
98

query I rowsort
SELECT distinct - col0 + 83 AS col1 FROM tab1 AS cor0
----
19
3
80

query I rowsort
SELECT - - col2 + 11 FROM tab1 AS cor0
----
107
65
68

query I rowsort
SELECT col1 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ALL - - col2 + - 16 FROM tab1 AS cor0
----
38
41
80

query I rowsort
SELECT distinct cor0.col0 AS col0 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT ALL + cor0.col0 FROM tab0, tab1 AS cor0
----
9 values hashing to dd18b93263a6cd425fc7cc84d9137870

query I rowsort
SELECT distinct col0 + col0 FROM tab0
----
178
48
70

query I rowsort
SELECT - ( col2 ) * - 7 FROM tab1
----
378
399
672

query I rowsort
SELECT - tab1.col1 * - ( 79 ) AS col0 FROM tab1, tab0 AS cor0
----
9 values hashing to 9f356c92ad187127dc66b1253be8643b

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab2 AS cor0, tab1
----
972 values hashing to 4c46de5c1773124597e14f3b372fc4ea

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col1 + - col1 col1 FROM tab2
----
0

query I rowsort
SELECT distinct col1 AS col1 FROM tab2
----
17
31
59

query I rowsort
SELECT ALL - ( - col0 ) * col1 * col0 + col2 FROM tab1 AS cor0
----
288
41017
83296

query I rowsort
SELECT col2 * col2 - col2 FROM tab0 AS cor0
----
0
1056
6642

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0, tab1 cor0
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query I rowsort
SELECT distinct col0 * col1 AS col2 FROM tab2
----
1343
217
4602

query I rowsort
SELECT - col0 * col1 - col0 * - col1 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT 88 AS col1 FROM tab2
----
88

query I rowsort
SELECT distinct 91 FROM tab1
----
91

query I rowsort
SELECT - - col1 * cor0.col0 AS col1 FROM tab1 AS cor0
----
1040
640
78

query I rowsort
SELECT col2 AS col1 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT 75 FROM tab2
----
75

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab1 AS cor1, tab0 AS cor2
----
972 values hashing to 9b91cf9fcc064ee1c13074a678b72ac7

query I rowsort
SELECT - - ( col2 ) + - col0 * - col1 AS col0 FROM tab0 AS cor0
----
2097
3396
8181

query I rowsort
SELECT 74 AS col1 FROM tab2
----
74

query I rowsort
SELECT ALL + col2 + col0 AS col1 FROM tab1 AS cor0
----
121
176
57

query I rowsort
SELECT - col1 * - col0 AS col0 FROM tab1
----
1040
640
78

query I rowsort
SELECT col1 + col1 FROM tab1 AS cor0
----
20
26
52

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab0 AS cor1, tab2 AS cor2
----
972 values hashing to 42e69ecdafb3c81046bc5cb4c98b1666

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0, tab0 AS cor1
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query IIIIII rowsort
SELECT distinct * FROM tab0 cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to 018801f36b33d2fe82cb95918ba502d6

query I rowsort
SELECT ALL + 63 AS col0 FROM tab2 AS cor0
----
63

query I rowsort
SELECT - - col1 * 65 + col1 FROM tab0 AS cor0
----
5676
6006
6402

query I rowsort
SELECT 79 FROM tab1 AS cor0
----
79

query I rowsort
SELECT - 64 * - col1 - col2 FROM tab0 AS cor0
----
5471
5742
6207

query I rowsort
SELECT ALL + tab0.col0 AS col1 FROM tab0
----
24
35
89

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0 CROSS JOIN tab1 AS cor1
----
243 values hashing to 70c6a01760d7239f3003db4da92180a4

query I rowsort
SELECT ALL + cor0.col0 FROM tab2 AS cor0
----
7
78
79

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0, tab1 AS cor0, tab2 AS cor1
----
972 values hashing to f0b9665afa0b835e4e5097af17c51766

query I rowsort
SELECT col0 + 44 AS col0 FROM tab0
----
133
68
79

query I rowsort
SELECT ALL - col1 + - col2 * - col1 FROM tab1 cor0
----
1235
1378
560

query I rowsort
SELECT - cor0.col1 + col1 FROM tab1 AS cor0
----
0
0
0

query I rowsort
SELECT ALL + col0 * col1 AS col1 FROM tab0 cor0
----
2064
3395
8099

query I rowsort
SELECT - - col0 AS col0 FROM tab0 AS cor0
----
24
35
89

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab1 AS cor1, tab1 AS cor2
----
972 values hashing to 635619591835474e6aa6acdff4ab166c

query I rowsort
SELECT col1 + col0 AS col0 FROM tab2
----
137
38
96

query I rowsort
SELECT ALL + ( 10 ) + col2 * cor0.col1 AS col0 FROM tab1 AS cor0
----
1258
1414
580

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0, tab2 AS cor1, tab0, tab2 AS cor2
----
3645 values hashing to 0c9c9a26da1b45580001288543ac8dbe

query IIIIIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab2, tab2 cor1
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query I rowsort
SELECT cor0.col2 + col2 FROM tab0 AS cor0
----
164
2
66

query I rowsort
SELECT 96 FROM tab1 cor0
----
96

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab2 cor1, tab0 AS cor2
----
972 values hashing to 63ccb67e72ebac679a0221202c067b9e

query I rowsort
SELECT 92 FROM tab2 AS cor0
----
92

query I rowsort
SELECT ALL + 64 FROM tab2
----
64

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 cor0, tab1 AS cor1
----
243 values hashing to 877a8dbac0e29b86e845fb64ed9d2242

query I rowsort
SELECT tab2.col0 FROM tab2, tab2 AS cor0
----
9 values hashing to 95b96ca1dbe2e39a0fa78f50d374f51a

query I rowsort
SELECT 37 * tab0.col1 FROM tab0, tab0 AS cor0
----
9 values hashing to 6e2d8808bd4257c36cb5fc1462c54827

query I rowsort
SELECT tab0.col1 FROM tab0, tab0 AS cor0
----
9 values hashing to 585a41a52c0c6c0d697b5d39265b74dc

query I rowsort
SELECT tab1.col0 + - col0 + 48 AS col0 FROM tab1
----
48
48
48

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 * col0 col2 FROM tab0
----
1225
576
7921

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab0 AS cor1, tab0 AS cor2
----
972 values hashing to 8420206d6932c454f05a38de634b3cb5

query IIIIIIIII rowsort
SELECT * FROM tab0, tab0 cor0, tab1 AS cor1
----
243 values hashing to 9ed1a6a444254225f040123c46b7f70c

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab0, tab0 cor1
----
972 values hashing to 3a31dab513390ca6bd05c71a3d9c50f0

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab0 AS cor1, tab0 AS cor2
----
972 values hashing to 09b120a8ff13ebafea7af10c2152241b

query I rowsort
SELECT ALL - col1 * - 20 * 12 FROM tab2 cor0
----
14160
4080
7440

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab1 AS cor0, tab2 AS cor1, tab0 AS cor2
----
972 values hashing to 95de14c88adc44eda4adb5267fe9ebd1

query I rowsort
SELECT ALL - col0 + col0 AS col2 FROM tab2
----
0
0
0

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab0 cor0
----
243 values hashing to 021da207cdc2a046fb0a79bf7cfc38ae

query I rowsort
SELECT 28 FROM tab0
----
28

query I rowsort
SELECT ALL + 11 FROM tab1 AS cor0
----
11

query I rowsort
SELECT - - 84 + col0 AS col1 FROM tab0 AS cor0
----
108
119
173

query I rowsort
SELECT distinct - - 82 FROM tab2 AS cor0
----
82

query I rowsort
SELECT 91 AS col0 FROM tab0
----
91

query I rowsort
SELECT ( 66 ) FROM tab1
----
66

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0, tab0 cor1
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query I rowsort
SELECT ALL - - 71 FROM tab0 AS cor0
----
71

query I rowsort
SELECT ALL + col0 * col0 FROM tab1 AS cor0
----
4096
6400
9

query I rowsort
SELECT cor0.col1 AS col0 FROM tab1 cor0
----
10
13
26

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab2 AS cor1, tab2, tab0 AS cor2
----
3645 values hashing to 5ec52b92c3c8d78cc0a61df3fc16f18b

query I rowsort
SELECT distinct - col0 * - col0 AS col0 FROM tab1 AS cor0
----
4096
6400
9

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL - ( - cor0.col1 ) + ( col2 ) col1 FROM tab2 AS cor0
----
55
58
85

query I rowsort
SELECT cor0.col1 + col0 AS col0 FROM tab0 cor0
----
110
132
180

query I rowsort
SELECT ALL + col1 AS col2 FROM tab0 cor0
----
86
91
97

query I rowsort
SELECT - - col0 AS col1 FROM tab0 cor0
----
24
35
89

query I rowsort
SELECT ALL - col1 - - col1 AS col1 FROM tab0
----
0
0
0

query I rowsort
SELECT col1 * col0 + ( - col0 ) AS col2 FROM tab2 AS cor0
----
1264
210
4524

query I rowsort
SELECT 25 FROM tab0 AS cor0
----
25

query I rowsort
SELECT ALL + - ( - cor0.col0 ) FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT distinct - 71 * - col0 FROM tab2 AS cor0
----
497
5538
5609

query I rowsort
SELECT ALL + col0 * col1 - - col1 AS col1 FROM tab2 AS cor0
----
1360
248
4661

query I rowsort
SELECT distinct 1 FROM tab1 AS cor0
----
1

query I rowsort
SELECT ( col2 ) * 29 FROM tab0 AS cor0
----
2378
29
957

query I rowsort
SELECT distinct col0 AS col0 FROM tab2
----
7
78
79

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col1 col0 FROM tab1
----
10
13
26

query I rowsort
SELECT tab1.col0 FROM tab1, tab1 AS cor0
----
9 values hashing to dd18b93263a6cd425fc7cc84d9137870

query I rowsort
SELECT - col2 * ( - col1 ) FROM tab1
----
1248
1404
570

query IIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab1 cor1
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query I rowsort
SELECT distinct - - 99 FROM tab0 AS cor0
----
99

query I rowsort
SELECT ALL + 19 FROM tab1 AS cor0
----
19

query I rowsort
SELECT distinct - - col2 + col1 AS col2 FROM tab2 AS cor0
----
55
58
85

query I rowsort
SELECT - col0 + 47 * col1 AS col1 FROM tab0 AS cor0
----
4018
4188
4524

query I rowsort
SELECT distinct 38 + cor0.col1 FROM tab0, tab1 AS cor0
----
48
51
64

query I rowsort
SELECT - - col2 * 29 AS col0 FROM tab0 AS cor0
----
2378
29
957

query I rowsort
SELECT distinct cor0.col1 AS col2 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT col1 * 63 FROM tab0 AS cor0
----
5418
5733
6111

query I rowsort
SELECT - - col2 FROM tab0 cor0
----
1
33
82

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col2 FROM tab2 AS cor0
----
17
31
59

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab1, tab1 cor0, tab1 AS cor1, tab0, tab0 AS cor2
----
3645 values hashing to 8db0cc6df185b737ff75d2626a6d198b

query I rowsort
SELECT cor0.col0 AS col1 FROM tab1, tab0 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query I rowsort
SELECT ALL + - 87 + col2 * col2 * 60 FROM tab2 AS cor0
----
40473
43653
86553

query I rowsort
SELECT ALL - 83 * - col0 + col2 FROM tab0 AS cor0
----
2025
2906
7469

query I rowsort
SELECT col1 * col1 FROM tab2 AS cor0
----
289
3481
961

query I rowsort
SELECT col2 * col2 AS col2 FROM tab2
----
1444
676
729

query I rowsort
SELECT cor0.col1 * 28 FROM tab1, tab0 AS cor0
----
9 values hashing to a332cfd25dcf64ec1aac7d898652e988

query I rowsort
SELECT cor0.col1 FROM tab2, tab2 AS cor0
----
9 values hashing to c61d27a0022e6d022371dc58819ab272

query I rowsort
SELECT distinct cor0.col1 FROM tab1, tab0 AS cor0
----
86
91
97

query I rowsort
SELECT distinct 21 AS col0 FROM tab1 AS cor0
----
21

query I rowsort
SELECT distinct - col1 + - col1 * - col1 FROM tab1 AS cor0
----
156
650
90

query I rowsort
SELECT ALL + 73 FROM tab2 AS cor0
----
73

query I rowsort
SELECT ALL - - col2 + - col2 AS col0 FROM tab2 cor0
----
0
0
0

query I rowsort
SELECT 78 * - cor0.col2 * - col2 + - cor0.col0 * col1 AS col2 FROM tab1 cor0
----
227370
252782
717808

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2, tab0 cor0
----
243 values hashing to 5c33e96b85afe1ea51bb6d4e9fa6f993

query I rowsort
SELECT tab0.col0 + col1 + col2 FROM tab0
----
133
143
262

query I rowsort
SELECT distinct - col0 * - col1 FROM tab1
----
1040
640
78

query I rowsort
SELECT col1 AS col1 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT col1 * col2 FROM tab2 AS cor0
----
1534
646
837

query I rowsort
SELECT distinct col2 * col0 AS col1 FROM tab1
----
162
3648
7680

query I rowsort
SELECT distinct - - 11 FROM tab0 AS cor0
----
11

query I rowsort
SELECT ALL - col0 * - col1 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT col0 * 7 + 78 AS col2 FROM tab1
----
526
638
99

query I rowsort
SELECT distinct col1 AS col1 FROM tab0 cor0
----
86
91
97

query I rowsort
SELECT distinct - 35 * - col2 AS col1 FROM tab1 AS cor0
----
1890
1995
3360

query I rowsort
SELECT distinct col2 * col1 + col2 FROM tab2 AS cor0
----
1560
684
864

query I rowsort
SELECT distinct - - col0 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT distinct 67 + col0 FROM tab1 cor0
----
131
147
70

query I rowsort
SELECT ALL + cor0.col0 AS col2 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT cor0.col1 * col0 AS col1 FROM tab1 cor0
----
1040
640
78

query I rowsort
SELECT ALL + col2 * col0 AS col1 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT - - col1 AS col1 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT ALL + cor0.col2 AS col0 FROM tab1, tab1 AS cor0
----
9 values hashing to 80ca0a1cc337a7714a8990a764cfdb17

query I rowsort
SELECT distinct col2 + cor0.col1 FROM tab0 cor0
----
119
173
98

query I rowsort
SELECT ALL + col0 + col2 FROM tab1 AS cor0
----
121
176
57

query I rowsort
SELECT col0 * col1 AS col2 FROM tab1
----
1040
640
78

query IIIIIIIIIIII rowsort
SELECT * FROM tab2 cor0 CROSS JOIN tab2, tab1 AS cor1, tab0 AS cor2
----
972 values hashing to e84152c0bf436177d3b3d80e42832d4f

query I rowsort
SELECT - - col2 FROM tab1 cor0
----
54
57
96

query I rowsort
SELECT col0 FROM tab1 cor0
----
3
64
80

query I rowsort
SELECT distinct - 86 * - 83 FROM tab0 AS cor0
----
7138

query I rowsort
SELECT col0 + col2 * col1 AS col2 FROM tab1 cor0
----
1328
1407
634

query I rowsort
SELECT ALL + col2 + col2 + - 66 FROM tab1 AS cor0
----
126
42
48

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab2 cor0, tab1
----
972 values hashing to 75a813ebd5ec5ec2e67a66d0593ff763

query I rowsort
SELECT - - col0 * ( cor0.col1 ) FROM tab1 cor0
----
1040
640
78

query I rowsort
SELECT distinct col2 AS col2 FROM tab0
----
1
33
82

query I rowsort
SELECT cor0.col0 + 68 AS col1 FROM tab2, tab1 AS cor0, tab0 AS cor1
----
27 values hashing to 4f5d4499e644681f67e840b4624c7612

query I rowsort
SELECT 69 FROM tab0 cor0
----
69

query I rowsort
SELECT 86 * - cor0.col0 * - col1 FROM tab1 AS cor0
----
55040
6708
89440

query I rowsort
SELECT ALL - - col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT ALL + 56 FROM tab0 cor0
----
56

query I rowsort
SELECT ALL + 27 AS col0 FROM tab0 AS cor0
----
27

query I rowsort
SELECT ALL + col0 AS col1 FROM tab1 cor0
----
3
64
80

query I rowsort
SELECT distinct - - col2 FROM tab0 AS cor0
----
1
33
82

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col1 col2 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT ALL + cor0.col1 AS col0 FROM tab0 AS cor0
----
86
91
97

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 cor0, tab1 AS cor1, tab2, tab2 AS cor2
----
3645 values hashing to 1a92b418ae3c05ba566f88a890a407ae

query I rowsort
SELECT cor0.col1 FROM tab0, tab0 AS cor0
----
9 values hashing to 585a41a52c0c6c0d697b5d39265b74dc

query I rowsort
SELECT col0 * col0 FROM tab2 AS cor0
----
49
6084
6241

query I rowsort
SELECT ( cor0.col2 ) AS col2 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT col2 * col1 + col1 FROM tab2 AS cor0
----
1593
663
868

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL - col0 col1 FROM tab2
----
4294967217
4294967218
4294967289

query I rowsort
SELECT distinct col1 * col1 FROM tab1 AS cor0
----
100
169
676

query I rowsort
SELECT cor1.col2 FROM tab2 AS cor0 CROSS JOIN tab1 cor1
----
9 values hashing to 80ca0a1cc337a7714a8990a764cfdb17

query I rowsort
SELECT col0 * cor0.col0 - col1 AS col1 FROM tab2 AS cor0
----
18
6025
6224

query I rowsort
SELECT distinct col1 AS col2 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT distinct 18 + cor0.col0 FROM tab2 AS cor0
----
25
96
97

query I rowsort
SELECT ( cor0.col0 ) AS col0 FROM tab1 cor0
----
3
64
80

query I rowsort
SELECT col1 * col1 + 42 * col0 FROM tab0 cor0
----
10879
12019
8404

query I rowsort
SELECT 31 * col1 FROM tab0
----
2666
2821
3007

query I rowsort
SELECT 57 FROM tab1 AS cor0
----
57

query I rowsort
SELECT ALL + ( cor0.col1 ) * cor2.col1 FROM tab0, tab0 AS cor0, tab0 AS cor1, tab1 AS cor2
----
81 values hashing to 9ef59267bc423612079185b5c4f6afb0

query I rowsort
SELECT 93 * cor0.col2 FROM tab0 AS cor0
----
3069
7626
93

query I rowsort
SELECT ( col0 ) AS col0 FROM tab1 cor0
----
3
64
80

query I rowsort
SELECT ALL + tab2.col0 FROM tab2, tab0 AS cor0
----
9 values hashing to 95b96ca1dbe2e39a0fa78f50d374f51a

query IIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab0, tab2 AS cor1
----
243 values hashing to ce53c0e8839c969b0513568da6eb2c4b

query I rowsort
SELECT distinct col2 AS col2 FROM tab2 cor0
----
26
27
38

query I rowsort
SELECT - 5 + col0 AS col0 FROM tab0 cor0
----
19
30
84

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab0, tab2 cor1, tab2 AS cor2, tab0 AS cor3
----
3645 values hashing to 35998cdc87c8b13ea047f14c9f5dc8d6

query IIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab0, tab0 AS cor1
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query I rowsort
SELECT col0 * 31 AS col2 FROM tab1
----
1984
2480
93

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 col1 FROM tab2
----
26
27
38

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1, tab2 AS cor0, tab0
----
972 values hashing to 58757c5bbbd4217c03cf2ac0b6126e55

query I rowsort
SELECT col1 * tab2.col0 * 15 FROM tab2
----
20145
3255
69030

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 cor0, tab0, tab1 AS cor1
----
972 values hashing to 0210050fb1701e2797a9b17e1ebac91e

query I rowsort
SELECT 2 FROM tab2
----
2

query I rowsort
SELECT col2 + col2 AS col0 FROM tab2
----
52
54
76

query I rowsort
SELECT col0 * col1 FROM tab1 AS cor0
----
1040
640
78

query I rowsort
SELECT ALL - ( - col1 + col1 ) * ( col1 ) AS col2 FROM tab1
----
0
0
0

query I rowsort
SELECT cor1.col0 + cor0.col1 FROM tab2, tab1 AS cor0, tab1 AS cor1
----
27 values hashing to 83cf0399a6d731112910be713c92fa44

query I rowsort
SELECT - - col2 FROM tab2 AS cor0
----
26
27
38

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 cor0, tab2 AS cor1
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query I rowsort
SELECT 47 FROM tab1 AS cor0
----
47

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0, tab1, tab0 AS cor1
----
972 values hashing to 5342fb4caf4767cb98bd21989bad099f

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0 CROSS JOIN tab0
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0 CROSS JOIN tab2, tab1 cor1
----
972 values hashing to 980274175fafec015a83080672486a9a

query I rowsort
SELECT cor0.col1 AS col2 FROM tab0, tab1 AS cor0
----
9 values hashing to 366ec539af0f37bd1519bc568f3d6775

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT tab1.col2 col2 FROM tab1, tab1 AS cor0
----
9 values hashing to 80ca0a1cc337a7714a8990a764cfdb17

query I rowsort
SELECT col0 + col0 AS col0 FROM tab0 cor0
----
178
48
70

query I rowsort
SELECT distinct col0 * cor0.col1 + - col2 AS col0 FROM tab1 AS cor0
----
24
583
944

query I rowsort
SELECT ALL - col0 + col1 FROM tab0 AS cor0
----
2
62
62

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + cor0.col1 col0 FROM tab2, tab2 AS cor0, tab1 AS cor1
----
27 values hashing to 7599b480125de521efed71b5b2413c7d

query I rowsort
SELECT ALL + col1 * col1 FROM tab0 AS cor0
----
7396
8281
9409

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 cor0, tab1 AS cor1
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2 cor0, tab2 AS cor1, tab2, tab1 AS cor2
----
3645 values hashing to 97b2ae21242e1e40418ee2ad06544f7a

query I rowsort
SELECT col2 + col1 * col1 FROM tab0 AS cor0
----
7429
8363
9410

query I rowsort
SELECT distinct - 35 + 41 AS col1 FROM tab0 AS cor0
----
6

query I rowsort
SELECT 11 + 9 * col2 FROM tab1 cor0
----
497
524
875

query I rowsort
SELECT distinct 0 AS col2 FROM tab1 AS cor0
----
0

query I rowsort
SELECT 59 * - 72 - col1 * cor0.col1 * - 95 FROM tab2 AS cor0
----
23207
326447
87047

query IIIIIIIII rowsort
SELECT * FROM tab1, tab1 cor0, tab0 AS cor1
----
243 values hashing to 3a953203ced079e372111d61dbd9e35f

query I rowsort
SELECT 71 * col1 FROM tab2
----
1207
2201
4189

query I rowsort
SELECT col0 * 40 FROM tab1 cor0
----
120
2560
3200

query I rowsort
SELECT distinct col2 + col1 FROM tab0 AS cor0
----
119
173
98

query I rowsort
SELECT ALL - col2 * - col0 FROM tab2 AS cor0
----
189
2028
3002

query I rowsort
SELECT - col2 + tab1.col2 AS col1 FROM tab1
----
0
0
0

query I rowsort
SELECT distinct col2 AS col0 FROM tab0
----
1
33
82

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 + col0 col0 FROM tab2
----
104
117
34

query I rowsort
SELECT distinct 33 FROM tab0
----
33

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 cor0, tab0 AS cor1, tab1 AS cor2
----
972 values hashing to 9af67d6f98010464af5d560bf949d487

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab2, tab0 AS cor1, tab0 AS cor2, tab2 AS cor3
----
3645 values hashing to ee83821bd928a072bc435d7135362ca1

query I rowsort
SELECT distinct - col0 + - col0 * - 58 AS col0 FROM tab2
----
399
4446
4503

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0, tab1 AS cor0, tab1 AS cor1
----
972 values hashing to 7864aada86bf5bf5e1621c7905de8dcd

query I rowsort
SELECT 68 AS col0 FROM tab0
----
68

query I rowsort
SELECT ALL - ( - tab1.col1 ) AS col0 FROM tab1
----
10
13
26

query I rowsort
SELECT - col1 * - col0 AS col1 FROM tab1
----
1040
640
78

query I rowsort
SELECT distinct - - col0 + cor0.col1 * col2 FROM tab1 cor0
----
1328
1407
634

query I rowsort
SELECT distinct ( col2 ) AS col1 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT col1 * col0 AS col1 FROM tab0 cor0
----
2064
3395
8099

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0 CROSS JOIN tab2, tab1 AS cor1
----
972 values hashing to 9364ef7545b07c67767dceb70f02c643

query I rowsort
SELECT 46 * cor0.col1 AS col2 FROM tab1 AS cor0
----
1196
460
598

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col2 + col0 col2 FROM tab2 AS cor0
----
104
117
34

query I rowsort
SELECT - col0 * - col1 * col2 FROM tab2 AS cor0
----
119652
51034
5859

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 cor0, tab2, tab0 AS cor1
----
972 values hashing to 95de14c88adc44eda4adb5267fe9ebd1

query I rowsort
SELECT ALL + col1 AS col0 FROM tab1
----
10
13
26

query IIIIIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab0, tab2 AS cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT distinct col2 * col0 AS col0 FROM tab2
----
189
2028
3002

query I rowsort
SELECT cor1.col2 FROM tab2 AS cor0 CROSS JOIN tab1, tab2 AS cor1
----
27 values hashing to 40fd8cc0de92ea68d73634c2d8f75bf5

query I rowsort
SELECT ALL + col2 AS col0 FROM tab2
----
26
27
38

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab1 cor1, tab2 cor2
----
972 values hashing to 2507aa9f48c3db94de9fec065edf3731

query I rowsort
SELECT distinct 46 FROM tab0
----
46

query I rowsort
SELECT distinct col1 + 36 FROM tab0
----
122
127
133

query I rowsort
SELECT ALL + cor0.col0 + - 6 AS col0 FROM tab0 AS cor0
----
18
29
83

query I rowsort
SELECT distinct col0 * 48 FROM tab1 AS cor0
----
144
3072
3840

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab1, tab2 AS cor1
----
972 values hashing to 0fcd8d0934383dd58863be894b07a6ed

query I rowsort
SELECT distinct - - col0 * cor0.col2 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT - - col0 + 83 FROM tab1 AS cor0
----
147
163
86

query I rowsort
SELECT cor0.col0 FROM tab0 AS cor0
----
24
35
89

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col0 col2 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT ALL + 58 FROM tab0 AS cor0
----
58

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0, tab0 cor1, tab0 AS cor2
----
972 values hashing to 8b4fcda7f1ca76bad7c7d728f54a51e0

query I rowsort
SELECT cor1.col1 AS col2 FROM tab2, tab0 cor0, tab0 AS cor1
----
27 values hashing to 2d6d3031dfe90e0c02db13aa63993bfd

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab2, tab2 AS cor1, tab1 AS cor2, tab1 AS cor3
----
3645 values hashing to 6156c969b7e054b8a333fdb86aee82f2

query I rowsort
SELECT - col1 + col1 FROM tab0 cor0
----
0
0
0

query I rowsort
SELECT ALL + 21 AS col2 FROM tab0 AS cor0
----
21

query I rowsort
SELECT col0 * - tab1.col2 * - col0 + 54 FROM tab1
----
233526
540
614454

query I rowsort
SELECT distinct 51 * col0 - ( - col2 ) * col2 FROM tab1
----
13296
3069
6513

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2, tab2 cor0
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

query I rowsort
SELECT col2 * col1 + col0 AS col0 FROM tab0 AS cor0
----
132
2862
7551

query I rowsort
SELECT distinct - - 40 + col2 * col1 AS col2 FROM tab2 AS cor0
----
1574
686
877

query I rowsort
SELECT - col1 * - col1 * ( col1 ) FROM tab2 AS cor0
----
205379
29791
4913

query I rowsort
SELECT - 4 - - col2 AS col1 FROM tab2 AS cor0
----
22
23
34

query IIIIII rowsort
SELECT distinct * FROM tab0 cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to b8667d60d280879b35ad1450a82b3a49

query I rowsort
SELECT distinct 47 * col2 AS col0 FROM tab2 AS cor0
----
1222
1269
1786

query I rowsort
SELECT ALL + col1 AS col0 FROM tab2 AS cor0
----
17
31
59

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - ( - col2 ) col0 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT ALL + - col1 * - cor0.col1 FROM tab0 AS cor0
----
7396
8281
9409

query I rowsort
SELECT distinct cor0.col1 AS col2 FROM tab0, tab1 AS cor0
----
10
13
26

query I rowsort
SELECT distinct - - ( col1 ) * col2 + cor0.col2 AS col2 FROM tab1 AS cor0
----
1344
1458
627

query I rowsort
SELECT distinct 38 FROM tab2 AS cor0
----
38

query I rowsort
SELECT 43 FROM tab2 cor0
----
43

query I rowsort
SELECT cor0.col1 + col1 FROM tab1 AS cor0
----
20
26
52

query I rowsort
SELECT distinct 65 FROM tab0
----
65

query I rowsort
SELECT - - cor0.col1 FROM tab1 AS cor0
----
10
13
26

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col2 col1 FROM tab1
----
54
57
96

query I rowsort
SELECT distinct col0 * col2 AS col0 FROM tab1
----
162
3648
7680

query I rowsort
SELECT tab2.col1 + tab2.col1 * tab2.col0 FROM tab2, tab1, tab1 AS cor0
----
27 values hashing to 09d904e364d7b9f14989070783f19e90

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col2 FROM tab0 AS cor0
----
86
91
97

query IIIIIIIII rowsort
SELECT distinct * FROM tab2 cor0 CROSS JOIN tab0, tab2 AS cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT col0 + 7 FROM tab0 AS cor0
----
31
42
96

query I rowsort
SELECT col0 + - 22 FROM tab0 AS cor0
----
13
2
67

query I rowsort
SELECT 86 * 81 AS col0 FROM tab1 AS cor0
----
6966

query I rowsort
SELECT col2 + col2 FROM tab0
----
164
2
66

query I rowsort
SELECT 67 AS col2 FROM tab0 AS cor0
----
67

query I rowsort
SELECT distinct 56 * col2 FROM tab2 AS cor0
----
1456
1512
2128

query I rowsort
SELECT 68 FROM tab2 AS cor0
----
68

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 - - col0 col1 FROM tab1 AS cor0
----
29
74
93

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab2 cor1, tab1, tab0 AS cor2
----
3645 values hashing to 9d746e15fdb5adcb43a7518cd9743eb3

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0, tab0 cor1, tab0 AS cor2
----
972 values hashing to d522b52b67b20888d3544d25cb98f232

query I rowsort
SELECT - - col2 + 23 FROM tab1 AS cor0
----
119
77
80

query I rowsort
SELECT col1 * col0 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT - - col2 + col2 AS col1 FROM tab1 AS cor0
----
108
114
192

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0 CROSS JOIN tab2
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

query IIIIIIIII rowsort
SELECT * FROM tab1, tab0 cor0 CROSS JOIN tab0
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query I rowsort
SELECT col2 + col1 AS col2 FROM tab2 WHERE NOT NULL NOT IN ( - col2 * col2 )
----

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - - cor0.col2 * col2 col1 FROM tab0 AS cor0
----
1
1089
6724

query I rowsort
SELECT distinct - col2 + col1 FROM tab0 AS cor0
----
53
9
96

query I rowsort
SELECT ALL + col0 + col1 AS col2 FROM tab0 cor0
----
110
132
180

query I rowsort
SELECT ALL + col0 * col0 AS col2 FROM tab0 AS cor0
----
1225
576
7921

query I rowsort
SELECT col0 * col0 + - col0 FROM tab0
----
1190
552
7832

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 cor0 CROSS JOIN tab0
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query I rowsort
SELECT - tab2.col2 * - col0 AS col1 FROM tab2
----
189
2028
3002

query I rowsort
SELECT ALL + col1 + col1 * col2 - col1 FROM tab0 cor0
----
2838
7462
97

query I rowsort
SELECT distinct col0 * col0 AS col1 FROM tab1
----
4096
6400
9

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 col2 FROM tab0
----
24
35
89

query I rowsort
SELECT ALL + col2 + - col1 * - col0 FROM tab1 AS cor0
----
1136
132
697

query I rowsort
SELECT distinct - col1 FROM tab1 cor0
----
4294967270
4294967283
4294967286

query I rowsort
SELECT distinct col0 AS col0 FROM tab1
----
3
64
80

query I rowsort
SELECT cor0.col2 AS col2 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT col2 * col0 AS col2 FROM tab0 cor0
----
35
7298
792

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT tab1.col0 * tab1.col2 col1 FROM tab1
----
162
3648
7680

query I rowsort
SELECT distinct tab0.col0 AS col2 FROM tab0
----
24
35
89

query I rowsort
SELECT distinct - col2 + - col2 * - col2 AS col2 FROM tab0
----
0
1056
6642

query I rowsort
SELECT col2 * col2 FROM tab2
----
1444
676
729

query I rowsort
SELECT tab0.col2 - tab0.col1 * - tab0.col1 FROM tab0
----
7429
8363
9410

query I rowsort
SELECT col2 + - col2 * - col2 FROM tab0
----
1122
2
6806

query I rowsort
SELECT distinct cor0.col1 + col1 AS col1 FROM tab1 AS cor0
----
20
26
52

query I rowsort
SELECT col0 * col2 * col0 AS col1 FROM tab0 AS cor0
----
1225
19008
649522

query I rowsort
SELECT distinct - col1 AS col0 FROM tab1 WHERE ( NULL ) = ( col0 )
----

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col0 * col1 col0 FROM tab2
----
1343
217
4602

query I rowsort
SELECT distinct - col1 * - col2 FROM tab1
----
1248
1404
570

query I rowsort
SELECT ALL + col1 + col1 * col0 FROM tab1
----
104
1053
650

query I rowsort
SELECT distinct tab2.col1 AS col1 FROM tab2
----
17
31
59

query I rowsort
SELECT tab2.col1 AS col1 FROM tab2
----
17
31
59

query I rowsort
SELECT - col0 + tab0.col2 * col0 AS col0 FROM tab0
----
0
7209
768

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0, tab0 AS cor1, tab0 AS cor2
----
972 values hashing to d522b52b67b20888d3544d25cb98f232

query I rowsort
SELECT distinct 69 FROM tab2
----
69

query I rowsort
SELECT distinct 44 FROM tab1
----
44

query I rowsort
SELECT 98 * col1 + col1 AS col0 FROM tab0 AS cor0
----
8514
9009
9603

query I rowsort
SELECT distinct - col0 + col0 FROM tab1
----
0

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 cor0 CROSS JOIN tab2
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query I rowsort
SELECT distinct 89 FROM tab2
----
89

query I rowsort
SELECT distinct col1 * 40 AS col1 FROM tab0
----
3440
3640
3880

query I rowsort
SELECT ALL - ( - ( col2 ) ) * 94 + cor0.col2 FROM tab0 AS cor0
----
3135
7790
95

query I rowsort
SELECT distinct - - cor0.col2 AS col0 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT distinct col2 - col2 AS col2 FROM tab2 AS cor0
----
0

query I rowsort
SELECT ALL + col1 * col0 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT ALL + - col1 + col0 * cor0.col2 FROM tab2 AS cor0
----
158
1969
2985

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + - col1 + col1 col1 FROM tab2 AS cor0
----
0
0
0

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col0 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT distinct 34 + tab1.col1 AS col1 FROM tab1
----
44
47
60

query I rowsort
SELECT ALL - - col0 * col1 + - col1 AS col0 FROM tab0 AS cor0
----
1978
3298
8008

query IIIIII rowsort
SELECT distinct * FROM tab1 AS cor0 CROSS JOIN tab0 cor1
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query IIIIIIIII rowsort
SELECT distinct * FROM tab0 AS cor0 CROSS JOIN tab2, tab2 AS cor1
----
243 values hashing to 5d85c5683e3ffd6d68920690d7302f7d

query I rowsort
SELECT col1 + col2 AS col1 FROM tab1
----
109
67
80

query I rowsort
SELECT distinct col1 * col2 AS col2 FROM tab1 AS cor0
----
1248
1404
570

query I rowsort
SELECT 96 AS col1 FROM tab0 AS cor0
----
96

query I rowsort
SELECT - col2 + col2 FROM tab0
----
0
0
0

query I rowsort
SELECT col0 AS col0 FROM tab0
----
24
35
89

query I rowsort
SELECT distinct - - 43 - cor0.col2 FROM tab0 AS cor0
----
10
42
4294967257

query I rowsort
SELECT distinct cor1.col1 + cor1.col1 FROM tab0 AS cor0 CROSS JOIN tab1 AS cor1
----
20
26
52

query I rowsort
SELECT distinct - - col0 + col1 * col1 FROM tab0 AS cor0
----
7420
8370
9444

query I rowsort
SELECT - 20 + col2 FROM tab2 AS cor0
----
18
6
7

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 + - ( - col2 ) col2 FROM tab1 AS cor0
----
109
67
80

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col0 * col1 col0 FROM tab1 AS cor0
----
1040
640
78

query I rowsort
SELECT ALL + cor0.col2 AS col0 FROM tab2, tab2 AS cor0
----
9 values hashing to 5911bac51441f4ff640b2a2b721ea8e3

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0, tab1 cor1, tab0 AS cor2
----
972 values hashing to 95920403df268a272c4e933cd0bbe0be

query IIIIIIIII rowsort
SELECT * FROM tab0 AS cor0 CROSS JOIN tab0, tab1 AS cor1
----
243 values hashing to 9ed1a6a444254225f040123c46b7f70c

query I rowsort
SELECT ALL + col0 AS col0 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT distinct - col2 * - col0 FROM tab0 AS cor0
----
35
7298
792

query I rowsort
SELECT cor0.col0 FROM tab2, tab1 cor0, tab0 AS cor1
----
27 values hashing to 778b50575a9b91448119ee0ee1a9c44f

query I rowsort
SELECT distinct - ( - tab0.col1 ) + col1 AS col0 FROM tab0
----
172
182
194

query I rowsort
SELECT distinct col2 + col2 AS col1 FROM tab2
----
52
54
76

query I rowsort
SELECT tab2.col1 - - col0 FROM tab2
----
137
38
96

query I rowsort
SELECT col2 * col0 FROM tab0 AS cor0
----
35
7298
792

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT tab0.col2 col1 FROM tab0, tab1 AS cor0
----
9 values hashing to c8f9fa9ef0f8702bd382e821378a96d8

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - - col2 - col1 col2 FROM tab1 AS cor0
----
28
47
83

query I rowsort
SELECT ALL - - cor0.col1 FROM tab2 AS cor0
----
17
31
59

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 cor0, tab1 AS cor1
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query I rowsort
SELECT - 9 + ( col1 ) FROM tab1 AS cor0
----
1
17
4

query I rowsort
SELECT distinct col0 + 55 * 75 + col2 AS col0 FROM tab0
----
4161
4182
4296

query I rowsort
SELECT ( col0 ) * col0 - - 26 FROM tab2 AS cor0
----
6110
6267
75

query I rowsort
SELECT distinct ( - col2 ) + col2 FROM tab1 AS cor0
----
0
39
4294967257

query I rowsort
SELECT 76 + - col2 + col0 AS col1 FROM tab2
----
117
128
56

query I rowsort
SELECT col1 * 65 + col0 + 9 AS col1 FROM tab1 AS cor0
----
1702
723
934

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1 cor0, tab0 AS cor1
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query I rowsort
SELECT ALL - - 22 AS col1 FROM tab1 AS cor0
----
22

query I rowsort
SELECT ALL - - col2 * col2 AS col0 FROM tab2 AS cor0
----
1444
676
729

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab1 AS cor0, tab0 cor1
----
972 values hashing to 67c5300bc5cba0be4f54a444dc6f05b9

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab0 cor1
----
243 values hashing to 566180e0144350a78b0ef3318e8f4c00

query I rowsort
SELECT ALL + col0 AS col0 FROM tab0 cor0
----
24
35
89

query I rowsort
SELECT distinct col1 * col1 FROM tab1 cor0
----
100
169
676

query I rowsort
SELECT ALL + - col0 * col1 + col1 AS col0 FROM tab1 AS cor0
----
4294966269
4294966666
4294967244

query I rowsort
SELECT ALL + cor0.col0 FROM tab0, tab0 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query I rowsort
SELECT cor0.col2 FROM tab2, tab0, tab0 AS cor0
----
27 values hashing to 7786718bd8042022537378d40ec87475

query I rowsort
SELECT distinct col1 AS col2 FROM tab2
----
17
31
59

query IIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab0, tab2 AS cor1
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT distinct tab1.col1 FROM tab1
----
10
13
26

query I rowsort
SELECT - - col0 AS col2 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT distinct 81 FROM tab1 cor0
----
81

query I rowsort
SELECT distinct ( col2 ) FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT col1 + tab2.col0 + col1 FROM tab2
----
113
196
69

query I rowsort
SELECT - ( - col1 ) AS col1 FROM tab0
----
86
91
97

query I rowsort
SELECT distinct col0 + col2 FROM tab1 AS cor0
----
121
176
57

query I rowsort
SELECT ALL - col2 * col0 - - col0 * col1 * col2 FROM tab0 cor0
----
3360
656820
67320

query I rowsort
SELECT distinct ( col0 ) FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT distinct - tab1.col1 - tab1.col2 * - col0 FROM tab1
----
136
3638
7667

query I rowsort
SELECT 2 AS col2 FROM tab2 cor0
----
2

query I rowsort
SELECT cor0.col2 AS col2 FROM tab1, tab0 AS cor0
----
9 values hashing to c8f9fa9ef0f8702bd382e821378a96d8

query I rowsort
SELECT cor0.col2 AS col1 FROM tab1, tab1 AS cor0
----
9 values hashing to 80ca0a1cc337a7714a8990a764cfdb17

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - col2 - col2 * - col0 col1 FROM tab0 cor0
----
34
7216
759

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT cor0.col0 col0 FROM tab2, tab1 AS cor0
----
9 values hashing to dd18b93263a6cd425fc7cc84d9137870

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab1 AS cor1, tab2 AS cor2
----
972 values hashing to 2507aa9f48c3db94de9fec065edf3731

query I rowsort
SELECT ALL - - col1 AS col2 FROM tab0 AS cor0
----
86
91
97

query IIIIIIIII rowsort
SELECT * FROM tab2, tab0 AS cor0 CROSS JOIN tab1
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query I rowsort
SELECT ALL - - col2 + - col2 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT ALL + 79 AS col2 FROM tab0 AS cor0
----
79

query I rowsort
SELECT - 47 * - cor0.col1 + cor0.col1 FROM tab0 AS cor0
----
4128
4368
4656

query I rowsort
SELECT - - col1 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT cor0.col0 + cor0.col2 AS col2 FROM tab2 AS cor0
----
104
117
34

query I rowsort
SELECT - - 68 + col1 FROM tab2 AS cor0
----
127
85
99

query I rowsort
SELECT ALL + col1 FROM tab1 cor0
----
10
13
26

query I rowsort
SELECT ALL + col1 + - col0 FROM tab0 AS cor0
----
2
62
62

query I rowsort
SELECT ALL + col1 + col1 FROM tab0 AS cor0
----
172
182
194

query I rowsort
SELECT ( col0 ) * cor0.col0 AS col0 FROM tab1 AS cor0
----
4096
6400
9

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col1 FROM tab1
----
10
13
26

query I rowsort
SELECT cor0.col2 AS col0 FROM tab0, tab2, tab0 AS cor0
----
27 values hashing to 7786718bd8042022537378d40ec87475

query I rowsort
SELECT col0 * col2 + 87 FROM tab0
----
122
7385
879

query I rowsort
SELECT ALL + col1 FROM tab1
----
10
13
26

query I rowsort
SELECT distinct 74 * col0 AS col1 FROM tab0
----
1776
2590
6586

query IIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0, tab1 cor1
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0, tab1 AS cor1, tab1 AS cor2
----
972 values hashing to ed80235f6457dada5cbb50ce9e2a8923

query I rowsort
SELECT - ( - col1 + - col2 ) AS col1 FROM tab2
----
55
58
85

query I rowsort
SELECT ( col0 ) FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT - - cor0.col0 AS col2 FROM tab1 cor0
----
3
64
80

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 cor0, tab1 AS cor1
----
243 values hashing to 2464a6f4cfabe66aeca50fcb4cd85bf5

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 cor0, tab2 AS cor1
----
243 values hashing to 60bd71ee2159222231bb3b5819bc5dca

query I rowsort
SELECT cor0.col2 + col1 AS col1 FROM tab2 AS cor0
----
55
58
85

query I rowsort
SELECT cor0.col0 FROM tab2 cor0
----
7
78
79

query I rowsort
SELECT cor0.col0 FROM tab1, tab2 cor0
----
9 values hashing to 95b96ca1dbe2e39a0fa78f50d374f51a

query I rowsort
SELECT - tab1.col2 AS col0 FROM tab1
----
4294967200
4294967239
4294967242

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab0 AS cor0, tab1 cor1
----
972 values hashing to 5621675b1bd32b061d284d0444c76601

query I rowsort
SELECT - - 6 + 8 FROM tab0 AS cor0
----
14

query I rowsort
SELECT 74 AS col1 FROM tab0 AS cor0
----
74

query I rowsort
SELECT 37 FROM tab1 cor0
----
37

query I rowsort
SELECT distinct 27 AS col2 FROM tab0
----
27

query I rowsort
SELECT - ( - 96 ) FROM tab2
----
96

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0, tab0, tab2 AS cor1
----
972 values hashing to e486ce227b61d9db6f8414f9d6361094

query I rowsort
SELECT distinct col0 AS col2 FROM tab1 AS cor0
----
3
64
80

query IIIIIIIII rowsort
SELECT * FROM tab2, tab2 AS cor0 CROSS JOIN tab0
----
243 values hashing to b3323704f6873113d863f8e27386b356

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0 CROSS JOIN tab1, tab2 AS cor1
----
972 values hashing to 01a5931cccc3dad8792a1bc6df09c614

query I rowsort
SELECT col0 * tab1.col0 FROM tab1
----
4096
6400
9

query I rowsort
SELECT - col0 + col1 FROM tab0
----
2
62
62

query I rowsort
SELECT distinct tab2.col2 AS col1 FROM tab2
----
26
27
38

query I rowsort
SELECT distinct col1 AS col1 FROM tab2 AS cor0
----
17
31
59

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + cor0.col0 col1 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT ALL + col0 AS col1 FROM tab0 AS cor0
----
24
35
89

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col0 + col1 col1 FROM tab1
----
29
74
93

query I rowsort
SELECT ALL + col0 + tab1.col2 AS col2 FROM tab1
----
121
176
57

query I rowsort
SELECT distinct col2 + col0 AS col0 FROM tab1
----
121
176
57

query I rowsort
SELECT col0 + col1 * col0 FROM tab2
----
1422
224
4680

query I rowsort
SELECT distinct col2 + col2 AS col0 FROM tab1 AS cor0
----
108
114
192

query I rowsort
SELECT distinct col0 * col0 FROM tab2 AS cor0
----
49
6084
6241

query I rowsort
SELECT - 78 + col1 * col0 FROM tab2
----
1265
139
4524

query I rowsort
SELECT ALL - 34 * - col1 AS col0 FROM tab1 AS cor0
----
340
442
884

query I rowsort
SELECT distinct 31 * col2 FROM tab2 cor0
----
1178
806
837

query I rowsort
SELECT ( col1 ) + col1 AS col2 FROM tab0
----
172
182
194

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col0 + col2 + - col0 col2 FROM tab1
----
54
57
96

query I rowsort
SELECT col2 * col0 AS col0 FROM tab1
----
162
3648
7680

query I rowsort
SELECT ALL - col0 * - col0 + tab2.col2 FROM tab2
----
6110
6279
76

query I rowsort
SELECT - col1 * - col1 AS col2 FROM tab0
----
7396
8281
9409

query I rowsort
SELECT col1 * - tab0.col0 FROM tab0 WHERE col2 <> NULL
----
4294959197
4294963901
4294965232

query I rowsort
SELECT col2 * col0 AS col1 FROM tab0
----
35
7298
792

query I rowsort
SELECT distinct col0 + col0 AS col2 FROM tab0
----
178
48
70

query III rowsort
SELECT * FROM tab2 WHERE ( NULL ) > NULL
----

query I rowsort
SELECT distinct col0 + col2 * col2 FROM tab1
----
2919
3313
9296

query III rowsort
SELECT * FROM tab1 WHERE col2 >= ( NULL )
----
9 values hashing to 8d6692e6d41505c3ad42d919bd9ecd0d

query I rowsort
SELECT distinct col0 + col0 AS col2 FROM tab2 AS cor0
----
14
156
158

query I rowsort
SELECT col1 + - col2 FROM tab0 AS cor0
----
53
9
96

query I rowsort
SELECT distinct cor0.col0 AS col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT cor0.col1 AS col0 FROM tab2, tab0 AS cor0
----
9 values hashing to 585a41a52c0c6c0d697b5d39265b74dc

query I rowsort
SELECT distinct cor0.col0 FROM tab0, tab0 AS cor0
----
24
35
89

query I rowsort
SELECT - - 44 AS col0 FROM tab0 AS cor0
----
44

query I rowsort
SELECT distinct 73 AS col0 FROM tab0 AS cor0
----
73

query I rowsort
SELECT col1 * col0 - - col0 FROM tab2 AS cor0
----
1422
224
4680

query IIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab0 cor1
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query I rowsort
SELECT - col2 * - col0 AS col1 FROM tab0 cor0
----
35
7298
792

query I rowsort
SELECT ALL + col1 * 81 FROM tab2
----
1377
2511
4779

query I rowsort
SELECT cor1.col2 FROM tab1 AS cor0 CROSS JOIN tab0 cor1
----
9 values hashing to c8f9fa9ef0f8702bd382e821378a96d8

query I rowsort
SELECT - col2 + col2 FROM tab2 AS cor0
----
0
0
0

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col1 col0 FROM tab0
----
86
91
97

query I rowsort
SELECT distinct col2 + 86 * col1 * col1 + col2 AS col0 FROM tab1
----
14726
58244
8714

query I rowsort
SELECT col2 * col2 * col0 FROM tab0
----
26136
35
598436

query IIIIIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab0, tab1 cor1
----
243 values hashing to 26173f1193178352de9a2e4ca7f09d53

query IIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab0, tab1 cor1
----
243 values hashing to 70c6a01760d7239f3003db4da92180a4

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab1 cor1
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query I rowsort
SELECT - 37 * - col1 FROM tab2 cor0
----
1147
2183
629

query IIIIIIIII rowsort
SELECT * FROM tab0 cor0 CROSS JOIN tab1, tab1 AS cor1
----
243 values hashing to 7e12d99d8ab63d9fd10e95cef9d78998

query I rowsort
SELECT distinct tab1.col0 FROM tab1
----
3
64
80

query I rowsort
SELECT cor0.col2 * 70 FROM tab0 AS cor0
----
2310
5740
70

query I rowsort
SELECT tab2.col2 * col2 * col1 FROM tab2
----
22599
24548
39884

query I rowsort
SELECT distinct - col0 + col2 * 57 FROM tab1
----
3075
3185
5392

query I rowsort
SELECT distinct 87 * col0 FROM tab2
----
609
6786
6873

query I rowsort
SELECT 42 * col2 - 37 FROM tab0 AS cor0
----
1349
3407
5

query I rowsort
SELECT tab0.col2 + col0 FROM tab0
----
171
36
57

query I rowsort
SELECT ALL + cor0.col2 * col2 AS col1 FROM tab0 AS cor0
----
1
1089
6724

query I rowsort
SELECT distinct col2 AS col2 FROM tab0 cor0
----
1
33
82

query I rowsort
SELECT ALL + cor0.col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT - cor0.col0 * - col1 AS col2 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT ALL - cor0.col0 * - col1 + cor0.col1 AS col0 FROM tab1 AS cor0
----
104
1053
650

query I rowsort
SELECT col1 + ( 80 + - col2 ) FROM tab0 cor0
----
133
176
89

query I rowsort
SELECT ALL + col1 AS col1 FROM tab0
----
86
91
97

query I rowsort
SELECT distinct - - col0 AS col0 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT distinct col2 AS col1 FROM tab2
----
26
27
38

query I rowsort
SELECT ALL - - cor0.col2 AS col2 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT ALL - col1 * - 2 FROM tab2 AS cor0
----
118
34
62

query I rowsort
SELECT ALL - ( - 68 ) FROM tab2 AS cor0
----
68

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - col2 + col2 * col0 col0 FROM tab2 cor0
----
162
2002
2964

query I rowsort
SELECT ALL - col2 + - col0 * - col2 AS col2 FROM tab0 AS cor0
----
34
7216
759

query I rowsort
SELECT 14 + col2 * col0 FROM tab2 AS cor0
----
203
2042
3016

query I rowsort
SELECT distinct col1 AS col1 FROM tab2 cor0
----
17
31
59

query I rowsort
SELECT distinct - - col0 * col2 AS col0 FROM tab1 AS cor0
----
162
3648
7680

query I rowsort
SELECT ALL + cor0.col2 * col2 AS col0 FROM tab0 AS cor0
----
1
1089
6724

query I rowsort
SELECT tab0.col2 + 5 FROM tab0
----
38
6
87

query I rowsort
SELECT distinct 52 * col0 FROM tab0
----
1248
1820
4628

query I rowsort
SELECT distinct col1 * col0 + cor0.col1 * col2 * col2 FROM tab1 AS cor0
----
120848
33130
75894

query I rowsort
SELECT ALL + col2 AS col1 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT ALL + 14 * col1 + 3 AS col0 FROM tab1 AS cor0
----
143
185
367

query I rowsort
SELECT col2 * col2 FROM tab0
----
1
1089
6724

query I rowsort
SELECT ALL - col0 + - 76 * - col1 AS col2 FROM tab0
----
6512
6827
7337

query IIIIII rowsort
SELECT distinct * FROM tab2 cor0 CROSS JOIN tab1 AS cor1
----
54 values hashing to 69e208df4a305efdfcc036bb4b31e720

query I rowsort
SELECT cor0.col2 FROM tab1, tab1 AS cor0
----
9 values hashing to 80ca0a1cc337a7714a8990a764cfdb17

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 AS cor0, tab1 cor1
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query I rowsort
SELECT 27 * col2 * col2 + col2 * - 99 AS col2 FROM tab1
----
239328
73386
82080

query I rowsort
SELECT distinct col0 * ( col0 ) AS col1 FROM tab0 cor0
----
1225
576
7921

query IIIIIIIIIIIIIIIIII rowsort
SELECT * FROM tab1 AS cor0 CROSS JOIN tab2, tab2 AS cor1, tab0, tab0 AS cor2, tab1
----
13122 values hashing to 91914e1516bd74d1b537b3edd58ebcd3

query I rowsort
SELECT distinct tab2.col2 FROM tab2, tab0 cor0
----
26
27
38

query I rowsort
SELECT 74 * 5 * col2 FROM tab1 AS cor0
----
19980
21090
35520

query I rowsort
SELECT cor0.col0 FROM tab2, tab2 AS cor0
----
9 values hashing to 95b96ca1dbe2e39a0fa78f50d374f51a

query IIIIIIIII rowsort
SELECT * FROM tab2, tab2 cor0, tab1 AS cor1
----
243 values hashing to 877a8dbac0e29b86e845fb64ed9d2242

query I rowsort
SELECT ALL + cor0.col2 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT ALL + col2 + 97 * cor0.col1 FROM tab0 AS cor0
----
8375
8909
9410

query I rowsort
SELECT ALL + cor0.col2 * 74 FROM tab2 AS cor0
----
1924
1998
2812

query I rowsort
SELECT 60 FROM tab1 AS cor0
----
60

query I rowsort
SELECT distinct tab1.col2 * col2 FROM tab1
----
2916
3249
9216

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - - cor0.col2 col1 FROM tab1 cor0
----
54
57
96

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 cor0, tab1 AS cor1
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query I rowsort
SELECT distinct 79 * col2 AS col0 FROM tab2
----
2054
2133
3002

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1, tab0 cor0, tab2
----
972 values hashing to a9068b700464993db9fae6f630605fde

query I rowsort
SELECT ALL + col0 * col2 AS col1 FROM tab2
----
189
2028
3002

query I rowsort
SELECT ( col1 ) * col2 FROM tab2
----
1534
646
837

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col1 + col2 col2 FROM tab0 AS cor0
----
119
173
98

query I rowsort
SELECT - col2 * - col1 FROM tab0
----
2838
7462
97

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0 cor0, tab2 AS cor1, tab2, tab0 AS cor2
----
3645 values hashing to 35998cdc87c8b13ea047f14c9f5dc8d6

query I rowsort
SELECT distinct - col2 * - col1 + tab2.col1 + tab2.col1 FROM tab2
----
1652
680
899

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col2 col0 FROM tab0
----
1
33
82

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab0, tab1 AS cor0, tab1
----
972 values hashing to 7864aada86bf5bf5e1621c7905de8dcd

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2, tab1 cor0
----
243 values hashing to 4fe4780e49e612b93957f575d9b3e89f

query I rowsort
SELECT - col2 * ( - 46 ) FROM tab1
----
2484
2622
4416

query I rowsort
SELECT col0 + ( col2 ) FROM tab1
----
121
176
57

query I rowsort
SELECT ALL - - col0 AS col2 FROM tab1 cor0
----
3
64
80

query I rowsort
SELECT ALL + col1 * col1 AS col0 FROM tab1 AS cor0
----
100
169
676

query I rowsort
SELECT - col2 + col2 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT distinct cor1.col0 - 1 FROM tab2, tab2 AS cor0, tab1 cor1
----
2
63
79

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT cor0.col0 col2 FROM tab1, tab2, tab0 AS cor0, tab0
----
81 values hashing to 2304fcc140e955eb2d1ee28ab1eea994

query I rowsort
SELECT 28 FROM tab1
----
28

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 cor0, tab2, tab1 AS cor1
----
972 values hashing to 4c46de5c1773124597e14f3b372fc4ea

query IIIIII rowsort
SELECT distinct * FROM tab2 cor0 CROSS JOIN tab2 AS cor1
----
54 values hashing to fe43263cad63144a098cccb9cd58c32a

query I rowsort
SELECT cor0.col2 AS col1 FROM tab0, tab1 AS cor0
----
9 values hashing to 80ca0a1cc337a7714a8990a764cfdb17

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab1, tab0 cor0
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query I rowsort
SELECT ALL + ( col1 ) + - col0 AS col0 FROM tab0 AS cor0
----
2
62
62

query I rowsort
SELECT - - 96 AS col0 FROM tab0 AS cor0
----
96

query I rowsort
SELECT distinct - col1 + col1 AS col2 FROM tab0
----
0

query IIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab2 cor1
----
243 values hashing to ea21cea53be47edd19229592e3d26141

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0, tab2 AS cor1, tab1 AS cor2
----
972 values hashing to 4634d10e8b6b37510bb99745aade36ab

query I rowsort
SELECT distinct col2 + col1 AS col2 FROM tab2
----
55
58
85

query I rowsort
SELECT col2 * col0 + col2 FROM tab0
----
36
7380
825

query I rowsort
SELECT - cor0.col0 * - col2 + - col0 AS col1 FROM tab1 cor0
----
159
3584
7600

query I rowsort
SELECT col1 AS col2 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ALL + cor0.col2 FROM tab2 cor0
----
26
27
38

query I rowsort
SELECT distinct - - col2 + - col2 FROM tab0 AS cor0
----
0

query I rowsort
SELECT ALL + tab0.col1 * col1 FROM tab0
----
7396
8281
9409

query I rowsort
SELECT col1 * 25 AS col0 FROM tab1 AS cor0
----
250
325
650

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1, tab0 cor0
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query I rowsort
SELECT distinct - - 83 FROM tab0 AS cor0
----
83

query I rowsort
SELECT ALL + 21 AS col0 FROM tab0 AS cor0
----
21

query I rowsort
SELECT col2 - - col2 FROM tab1 AS cor0
----
108
114
192

query IIIIII rowsort
SELECT * FROM tab0 cor0 CROSS JOIN tab1 cor1
----
54 values hashing to b010e320d66ab5b2711fc14e8fb58b01

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 cor0, tab2 AS cor1
----
243 values hashing to 2248b8c3b6efacb4e8fc6d9f81b7df8b

query I rowsort
SELECT 62 AS col2 FROM tab0
----
62

query I rowsort
SELECT ALL + col0 AS col2 FROM tab0 cor0
----
24
35
89

query I rowsort
SELECT col2 * col0 FROM tab2 cor0
----
189
2028
3002

query I rowsort
SELECT distinct - 19 - - 56 FROM tab0
----
37

query I rowsort
SELECT col2 + 28 * col0 AS col0 FROM tab2
----
2210
223
2250

query I rowsort
SELECT ALL + 80 AS col2 FROM tab2
----
80

query I rowsort
SELECT - col2 + col1 AS col0 FROM tab0 AS cor0
----
53
9
96

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0 AS cor0, tab2, tab2 AS cor1
----
972 values hashing to a698694a7dac245e42212ff0316bdf45

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab0, tab2 AS cor1
----
972 values hashing to 42e69ecdafb3c81046bc5cb4c98b1666

query IIIIIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab1, tab1 cor1
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query IIIIII rowsort
SELECT * FROM tab2 cor0 CROSS JOIN tab0 cor1
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query I rowsort
SELECT - - col0 + - 16 * - 15 FROM tab1 AS cor0
----
243
304
320

query I rowsort
SELECT 85 FROM tab1 AS cor0
----
85

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2 AS cor0, tab1, tab2 AS cor1
----
972 values hashing to bcf430f79386b43bc4077271fcd15cf0

query I rowsort
SELECT 4 * col0 AS col2 FROM tab1 AS cor0
----
12
256
320

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct cor0.col1 col2 FROM tab1 cor0
----
10
13
26

query I rowsort
SELECT ALL - - 16 AS col2 FROM tab0 AS cor0
----
16

query I rowsort
SELECT distinct - col0 * - col0 AS col1 FROM tab1 AS cor0
----
4096
6400
9

query I rowsort
SELECT ALL + 73 AS col0 FROM tab1 AS cor0
----
73

query I rowsort
SELECT - tab1.col2 * - col1 + col0 FROM tab1
----
1328
1407
634

query I rowsort
SELECT col2 * 1 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT col2 * 20 AS col0 FROM tab0 AS cor0
----
1640
20
660

query I rowsort
SELECT ALL + ( col2 ) AS col0 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT col0 - - col0 AS col0 FROM tab0
----
178
48
70

query I rowsort
SELECT ALL + col0 * col0 * col2 AS col0 FROM tab2 AS cor0
----
1323
158184
237158

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 AS cor0 CROSS JOIN tab1
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query I rowsort
SELECT ( col0 ) + - cor0.col0 AS col0 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT 89 * col2 + col0 AS col1 FROM tab2 AS cor0
----
2392
2410
3461

query I rowsort
SELECT ALL - - col1 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT ALL - - col1 + col2 AS col1 FROM tab2 AS cor0
----
55
58
85

query I rowsort
SELECT col2 + col2 * col0 AS col1 FROM tab1 cor0
----
216
3705
7776

query I rowsort
SELECT col2 + - cor0.col1 AS col2 FROM tab1 AS cor0
----
28
47
83

query I rowsort
SELECT ALL - col1 + ( col1 ) FROM tab1 AS cor0
----
0
0
0

query I rowsort
SELECT - col2 * - col2 FROM tab1
----
2916
3249
9216

query I rowsort
SELECT ALL + col2 * col0 * col1 AS col1 FROM tab1 AS cor0
----
36480
4212
99840

query I rowsort
SELECT - col0 * - col0 AS col2 FROM tab2
----
49
6084
6241

query I rowsort
SELECT - col0 + col1 * 42 AS col2 FROM tab1 cor0
----
1089
356
466

query I rowsort
SELECT col1 + - col1 AS col0 FROM tab1 AS cor0
----
0
0
0

query I rowsort
SELECT ALL + col2 * col0 FROM tab0
----
35
7298
792

query I rowsort
SELECT distinct cor0.col2 AS col0 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT - - col0 * col2 FROM tab0 AS cor0
----
35
7298
792

query I rowsort
SELECT ALL + col2 * col0 FROM tab0 cor0
----
35
7298
792

query I rowsort
SELECT distinct col2 + col2 FROM tab2 AS cor0
----
52
54
76

query I rowsort
SELECT - - col2 * col0 FROM tab2 AS cor0
----
189
2028
3002

query I rowsort
SELECT ALL - col0 * cor0.col0 * - cor0.col0 FROM tab1 AS cor0
----
262144
27
512000

query I rowsort
SELECT ALL - - col0 FROM tab2 cor0
----
7
78
79

query I rowsort
SELECT - 23 * - tab2.col2 AS col2 FROM tab2
----
598
621
874

query I rowsort
SELECT - ( col2 ) + - col1 * - 40 AS col1 FROM tab0 AS cor0
----
3407
3558
3879

query I rowsort
SELECT col1 AS col2 FROM tab2
----
17
31
59

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab1 AS cor1, tab0, tab2 AS cor2
----
3645 values hashing to 149298fc0224e93f3bc2df24a3ebeeb8

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 + col0 col1 FROM tab1 AS cor0
----
29
74
93

query I rowsort
SELECT - col0 * - col2 FROM tab2 AS cor0
----
189
2028
3002

query I rowsort
SELECT ALL + 85 AS col1 FROM tab1 cor0
----
85

query I rowsort
SELECT col1 AS col0 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT ( cor0.col2 ) AS col1 FROM tab0 AS cor0
----
1
33
82

query I rowsort
SELECT distinct col1 + col0 FROM tab2
----
137
38
96

query I rowsort
SELECT cor0.col2 + col0 FROM tab0 AS cor0
----
171
36
57

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 AS cor0, tab0 cor1
----
243 values hashing to b3323704f6873113d863f8e27386b356

query I rowsort
SELECT col1 * 77 + col0 FROM tab0
----
6646
7096
7504

query I rowsort
SELECT ALL - ( - col1 ) FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT col0 * col0 AS col1 FROM tab0 AS cor0
----
1225
576
7921

query I rowsort
SELECT col1 * col0 FROM tab2 AS cor0
----
1343
217
4602

query I rowsort
SELECT - col0 * - col1 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT ALL + 30 AS col0 FROM tab0
----
30

query I rowsort
SELECT ALL + 86 FROM tab1
----
86

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - col1 * - col0 col2 FROM tab1 cor0
----
1040
640
78

query I rowsort
SELECT ALL + col2 AS col1 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT distinct 81 AS col0 FROM tab1 AS cor0
----
81

query I rowsort
SELECT - - col1 * col0 + col1 FROM tab2 AS cor0
----
1360
248
4661

query I rowsort
SELECT ALL + 59 + - 21 FROM tab1 AS cor0
----
38

query I rowsort
SELECT 85 AS col0 FROM tab1 AS cor0
----
85

query I rowsort
SELECT ALL - - col1 FROM tab1 cor0
----
10
13
26

query I rowsort
SELECT cor0.col1 FROM tab2 AS cor0
----
17
31
59

query IIIIIIIIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 AS cor0, tab2 cor1, tab0, tab2 AS cor2
----
3645 values hashing to fcae6e4467f798ac88c869b8e38c6b23

query I rowsort
SELECT distinct - col2 + ( col1 ) FROM tab0 AS cor0
----
53
9
96

query IIIIIIIIIIIIIII rowsort
SELECT distinct * FROM tab2, tab0 AS cor0, tab0 AS cor1, tab0, tab2 AS cor2
----
3645 values hashing to fa0488bdae83f58c7ffa92505e928570

query I rowsort
SELECT ALL + cor0.col1 AS col2 FROM tab0, tab2, tab0 AS cor0
----
27 values hashing to 2d6d3031dfe90e0c02db13aa63993bfd

query I rowsort
SELECT 33 FROM tab1 cor0
----
33

query I rowsort
SELECT col1 * 22 AS col0 FROM tab2 AS cor0
----
1298
374
682

query I rowsort
SELECT ALL - - col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT 78 * tab0.col0 * tab0.col2 AS col1 FROM tab0
----
2730
569244
61776

query I rowsort
SELECT 83 AS col0 FROM tab1
----
83

query I rowsort
SELECT col2 + col2 FROM tab1 AS cor0
----
108
114
192

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col2 col1 FROM tab0
----
1
33
82

query I rowsort
SELECT ALL + 80 AS col2 FROM tab1
----
80

query I rowsort
SELECT col1 * tab0.col2 FROM tab0
----
2838
7462
97

query IIIIII rowsort
SELECT distinct * FROM tab2 AS cor0 CROSS JOIN tab0 cor1
----
54 values hashing to 3352c458f45211cf9aa3236c2cd6dd38

query IIIIIIIII rowsort
SELECT * FROM tab2 AS cor0 CROSS JOIN tab1, tab0 AS cor1
----
243 values hashing to 2ba47a833971d4c4b0287e849fb0cfb8

query I rowsort
SELECT tab0.col1 * 86 FROM tab0, tab2 AS cor0, tab1 AS cor1
----
27 values hashing to 149415a063bb0f6819c6aede5bcaf735

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2, tab0 cor0, tab1 AS cor1
----
972 values hashing to 0210050fb1701e2797a9b17e1ebac91e

query I rowsort
SELECT ALL + col1 * col2 AS col0 FROM tab2 AS cor0
----
1534
646
837

query I rowsort
SELECT distinct col0 AS col0 FROM tab2 cor0
----
7
78
79

query I rowsort
SELECT distinct col1 + 96 * col2 AS col1 FROM tab2 AS cor0
----
2555
2623
3665

query I rowsort
SELECT ALL + col2 - - col1 AS col0 FROM tab2 AS cor0
----
55
58
85

query I rowsort
SELECT 67 AS col1 FROM tab2
----
67

query I rowsort
SELECT distinct tab1.col0 AS col1 FROM tab1
----
3
64
80

query I rowsort
SELECT - col2 * tab2.col0 + tab2.col2 * col0 FROM tab2
----
0
0
0

query I rowsort
SELECT col2 + col0 - - col2 AS col2 FROM tab2
----
130
155
61

query I rowsort
SELECT tab1.col1 AS col0 FROM tab1
----
10
13
26

query I rowsort
SELECT ALL + tab2.col1 AS col1 FROM tab2
----
17
31
59

query I rowsort
SELECT ALL + col2 FROM tab2
----
26
27
38

query I rowsort
SELECT col0 + col1 FROM tab0
----
110
132
180

query I rowsort
SELECT ALL + col0 + col0 FROM tab1
----
128
160
6

query I rowsort
SELECT ALL + col1 AS col2 FROM tab2
----
17
31
59

query I rowsort
SELECT ALL + ( col2 ) FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT col0 * col0 AS col1 FROM tab1 AS cor0
----
4096
6400
9

query I rowsort
SELECT distinct col1 + tab2.col1 AS col1 FROM tab2
----
118
34
62

query I rowsort
SELECT distinct col0 + col1 FROM tab2
----
137
38
96

query I rowsort
SELECT col0 + tab2.col1 FROM tab2 WHERE NOT NULL <> NULL
----
137
38
96

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 col1 FROM tab2
----
17
31
59

query I rowsort
SELECT tab1.col1 AS col2 FROM tab1
----
10
13
26

query I rowsort
SELECT distinct col0 * col1 AS col2 FROM tab1 AS cor0
----
1040
640
78

query I rowsort
SELECT ALL + 35 + col1 + 29 FROM tab2 AS cor0
----
123
81
95

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col2 col2 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT distinct col1 * cor0.col2 AS col0 FROM tab1 AS cor0
----
1248
1404
570

query I rowsort
SELECT tab0.col0 * tab0.col1 FROM tab0
----
2064
3395
8099

query I rowsort
SELECT 70 + col1 AS col0 FROM tab0
----
156
161
167

query I rowsort
SELECT distinct - col0 + cor0.col0 AS col1 FROM tab2 cor0
----
0

query I rowsort
SELECT col2 * - ( - col1 ) + - col1 + - col2 * - col1 FROM tab2
----
1275
1643
3009

query I rowsort
SELECT distinct col2 + col0 FROM tab0 cor0
----
171
36
57

query I rowsort
SELECT ALL - - 23 FROM tab1 AS cor0
----
23

query I rowsort
SELECT - col0 * - col0 FROM tab2
----
49
6084
6241

query I rowsort
SELECT 58 AS col2 FROM tab0 AS cor0
----
58

query IIIIIIIIIIIIIII rowsort
SELECT * FROM tab1, tab2 AS cor0, tab0 AS cor1, tab0, tab1 AS cor2
----
3645 values hashing to 25b043ae64f25e8f205735b09d2d3d6a

query I rowsort
SELECT cor0.col0 AS col2 FROM tab2, tab0 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query I rowsort
SELECT distinct - col1 * - cor0.col1 + cor0.col0 + 46 FROM tab2 AS cor0
----
1014
3605
414

query I rowsort
SELECT ALL + cor0.col0 + cor0.col2 FROM tab1 AS cor0
----
121
176
57

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT tab2.col1 col2 FROM tab2
----
17
31
59

query I rowsort
SELECT ALL + col0 * col2 AS col0 FROM tab1 cor0
----
162
3648
7680

query I rowsort
SELECT - - col0 AS col0 FROM tab2 AS cor0
----
7
78
79

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 * col0 col0 FROM tab0 AS cor0
----
2064
3395
8099

query I rowsort
SELECT 62 AS col0 FROM tab1 AS cor0
----
62

query I rowsort
SELECT - cor0.col1 * - col1 AS col2 FROM tab0 AS cor0
----
7396
8281
9409

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - ( - ( col1 ) ) col0 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT - col2 * - 88 AS col1 FROM tab0
----
2904
7216
88

query I rowsort
SELECT distinct - col2 + col1 AS col0 FROM tab0 AS cor0
----
53
9
96

query I rowsort
SELECT distinct - 69 * ( - col0 ) + col1 * cor0.col0 FROM tab1 AS cor0
----
285
5056
6560

query I rowsort
SELECT ( 23 ) * col2 + - col2 FROM tab0 AS cor0
----
1804
22
726

query I rowsort
SELECT - 27 * - col0 AS col1 FROM tab2
----
189
2106
2133

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab1 AS cor0 CROSS JOIN tab0 cor1
----
243 values hashing to 3a953203ced079e372111d61dbd9e35f

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab2, tab2 AS cor0, tab2 cor1
----
972 values hashing to a47a9db07c7de4927c7c28efb4cd13f2

query I rowsort
SELECT distinct tab0.col1 AS col1 FROM tab0
----
86
91
97

query I rowsort
SELECT distinct 21 * tab2.col1 FROM tab2, tab0 AS cor0, tab2 cor1
----
1239
357
651

query I rowsort
SELECT distinct col0 * 76 + col0 FROM tab0 AS cor0
----
1848
2695
6853

query I rowsort
SELECT tab0.col2 AS col2 FROM tab0, tab2 cor0
----
9 values hashing to c8f9fa9ef0f8702bd382e821378a96d8

query I rowsort
SELECT ALL + 9 AS col0 FROM tab1 AS cor0
----
9

query I rowsort
SELECT distinct - - 17 AS col1 FROM tab1 AS cor0
----
17

query I rowsort
SELECT cor0.col0 + col1 AS col2 FROM tab0 AS cor0
----
110
132
180

query I rowsort
SELECT - - col1 * col2 + col1 * col1 FROM tab1 AS cor0
----
1417
2080
670

query I rowsort
SELECT 93 * col0 FROM tab1
----
279
5952
7440

query I rowsort
SELECT - col1 + 79 * col0 - - cor0.col1 FROM tab2 AS cor0
----
553
6162
6241

query I rowsort
SELECT distinct - col0 + cor0.col0 * col1 FROM tab0 AS cor0
----
2040
3360
8010

query I rowsort
SELECT - col0 * - 46 + - col2 FROM tab2 cor0
----
295
3562
3596

query I rowsort
SELECT distinct cor0.col0 FROM tab0 cor0
----
24
35
89

query I rowsort
SELECT distinct col2 * col0 + - col1 FROM tab1 AS cor0
----
136
3638
7667

query I rowsort
SELECT distinct cor0.col0 FROM tab2, tab0 AS cor0, tab2 AS cor1
----
24
35
89

query I rowsort
SELECT distinct cor0.col2 + cor0.col2 FROM tab0, tab1 AS cor0
----
108
114
192

query I rowsort
SELECT ALL - ( col0 ) * - col0 + 10 FROM tab2
----
59
6094
6251

query I rowsort
SELECT distinct col0 + col2 * col0 FROM tab1
----
165
3712
7760

query I rowsort
SELECT distinct - col2 * - col0 * cor0.col2 FROM tab0 cor0
----
26136
35
598436

query I rowsort
SELECT ALL - col2 + col2 AS col0 FROM tab0 AS cor0
----
0
0
0

query I rowsort
SELECT col1 * col0 FROM tab2
----
1343
217
4602

query I rowsort
SELECT 76 * - col2 * - 88 + col0 * - tab0.col0 FROM tab0
----
220128
540495
5463

query I rowsort
SELECT ALL + 19 AS col2 FROM tab0 AS cor0
----
19

query I rowsort
SELECT col1 * col1 + - col1 FROM tab1
----
156
650
90

query I rowsort
SELECT col1 + - ( col1 ) AS col1 FROM tab1 AS cor0
----
0
0
0

query IIIIIIIII rowsort
SELECT distinct * FROM tab2, tab2 AS cor0 CROSS JOIN tab0
----
243 values hashing to b3323704f6873113d863f8e27386b356

query IIIIIIIIIIII rowsort
SELECT * FROM tab1, tab0 AS cor0 CROSS JOIN tab0, tab1 AS cor1
----
972 values hashing to 9af67d6f98010464af5d560bf949d487

query I rowsort
SELECT cor0.col0 * tab0.col0 FROM tab0, tab2 AS cor0
----
9 values hashing to 12930ec3ed2e24e506ebb47d036ed597

query I rowsort
SELECT ALL + col0 AS col0 FROM tab2
----
7
78
79

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2, tab1 cor0
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab1 AS cor0, tab1 AS cor1, tab0 AS cor2
----
972 values hashing to b51b4342db121ebc2d3d353dcd8ed521

query IIIIIIIII rowsort
SELECT * FROM tab1, tab2 cor0, tab2 AS cor1
----
243 values hashing to 042fa16c43ab365359ee93c064e44127

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct tab2.col1 + col2 col2 FROM tab2
----
55
58
85

query I rowsort
SELECT distinct 67 FROM tab0
----
67

query I rowsort
SELECT 26 FROM tab0
----
26

query I rowsort
SELECT - ( col1 ) + col1 AS col0 FROM tab1 cor0
----
0
0
0

query I rowsort
SELECT cor0.col2 * tab0.col2 FROM tab0, tab1 AS cor0
----
9 values hashing to 1e358219bf03c93d7085a65107d13cf1

query IIIIIIIII rowsort
SELECT distinct * FROM tab0, tab2 cor0, tab1 AS cor1
----
243 values hashing to 098e223d780e18b6582523fd6f55eec9

query I rowsort
SELECT 62 AS col1 FROM tab0
----
62

query I rowsort
SELECT cor0.col1 + cor0.col2 * cor0.col1 AS col2 FROM tab2 cor0
----
1593
663
868

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT - col0 * - ( col0 ) col1 FROM tab2 AS cor0
----
49
6084
6241

query I rowsort
SELECT distinct col0 * 83 + - col0 FROM tab0 cor0
----
1968
2870
7298

query I rowsort
SELECT ALL + col0 AS col2 FROM tab1 AS cor0
----
3
64
80

query I rowsort
SELECT distinct - - 77 FROM tab1 AS cor0
----
77

query I rowsort
SELECT 81 * col0 FROM tab0
----
1944
2835
7209

query IIIIIIIIIIII rowsort
SELECT * FROM tab0, tab0 AS cor0 CROSS JOIN tab1, tab1 AS cor1
----
972 values hashing to d222ba302bd1ddd1c8b2ddf1a4d0b07a

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab0, tab1 AS cor0, tab2, tab1 cor1
----
972 values hashing to dd771e0c15d524f62127686e9bd43f9a

query I rowsort
SELECT distinct 67 + col2 AS col2 FROM tab0
----
100
149
68

query I rowsort
SELECT tab1.col1 - - col0 AS col0 FROM tab1
----
29
74
93

query I rowsort
SELECT ( col2 ) * 46 AS col0 FROM tab2
----
1196
1242
1748

query IIIIIIIII rowsort
SELECT * FROM tab2, tab1 cor0, tab1 cor1
----
243 values hashing to 89e3b35a4a4f02d7b83645addb9dcdc3

query I rowsort
SELECT ALL + col1 * 89 + col2 AS col2 FROM tab1 AS cor0
----
1253
2368
947

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 + tab0.col2 col1 FROM tab0
----
119
173
98

query I rowsort
SELECT col1 + 77 FROM tab0
----
163
168
174

query I rowsort
SELECT cor1.col2 FROM tab2, tab0 cor0, tab0 AS cor1, tab0, tab2 AS cor2
----
243 values hashing to 291cdf20f55dc7bbcb55f561dc0b74d8

query I rowsort
SELECT distinct - col0 * - 13 FROM tab2
----
1014
1027
91

query IIIIIIIIIIII rowsort
SELECT distinct * FROM tab1, tab2 AS cor0, tab0, tab0 AS cor1
----
972 values hashing to 09b120a8ff13ebafea7af10c2152241b

query IIIIIIIIIIII rowsort
SELECT * FROM tab2, tab1 cor0 CROSS JOIN tab1, tab0 AS cor1
----
972 values hashing to 909b7ebab62aff8f69dc42ccbb5c2eae

query I rowsort
SELECT 52 * 60 AS col2 FROM tab2
----
3120

query IIIIIIIII rowsort
SELECT distinct * FROM tab1, tab0, tab0 cor0
----
243 values hashing to 3581f59ff9574f9d6290fc6bca0b5e4d

query I rowsort
SELECT distinct col1 + col0 + col2 FROM tab0 cor0
----
133
143
262

query I rowsort
SELECT - ( - col0 ) FROM tab2
----
7
78
79

query I rowsort
SELECT ( col2 ) AS col2 FROM tab2 cor0
----
26
27
38

query I rowsort
SELECT cor0.col2 - - col1 FROM tab2 AS cor0
----
55
58
85

query IIIIII rowsort
SELECT distinct * FROM tab1 cor0 CROSS JOIN tab0 AS cor1
----
54 values hashing to 2a7467bc6f55dbb61fbd4aa2bd0646a9

query I rowsort
SELECT distinct col1 - - cor0.col2 FROM tab0 AS cor0
----
119
173
98

query I rowsort
SELECT distinct 35 FROM tab0 AS cor0
----
35

query I rowsort
SELECT col0 * col2 - ( - col0 ) FROM tab0 AS cor0
----
70
7387
816

query I rowsort
SELECT ALL - - col1 AS col2 FROM tab1 AS cor0
----
10
13
26

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col1 col2 FROM tab2 AS cor0
----
17
31
59

query I rowsort
SELECT ALL + cor0.col0 + - col1 * - col0 FROM tab1 AS cor0
----
1120
704
81

query I rowsort
SELECT col0 AS col1 FROM tab2 AS cor0
----
7
78
79

query I rowsort
SELECT col1 * col0 + tab2.col2 FROM tab2
----
1381
244
4628

query I rowsort
SELECT - - col2 FROM tab1 AS cor0
----
54
57
96

query I rowsort
SELECT distinct - col2 + ( - col2 ) * - cor0.col2 FROM tab1 AS cor0
----
2862
3192
9120

query I rowsort
SELECT ALL - - col2 AS col1 FROM tab2 AS cor0
----
26
27
38

query I rowsort
SELECT ALL - col2 + - ( col1 ) + - col0 * - col1 AS col1 FROM tab2 AS cor0
----
1288
159
4517

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct - - col1 col0 FROM tab1 AS cor0
----
10
13
26

query I rowsort
SELECT - - cor0.col1 FROM tab0 AS cor0
----
86
91
97

query I rowsort
SELECT distinct 80 + col2 FROM tab1 AS cor0
----
134
137
176

query I rowsort
SELECT distinct col0 * col1 AS col0 FROM tab2 AS cor0
----
1343
217
4602

query I rowsort
SELECT 20 AS col0 FROM tab2 AS cor0
----
20

query I rowsort
SELECT col2 + cor0.col2 FROM tab1 AS cor0
----
108
114
192

query I rowsort
SELECT - cor0.col2 * - col1 FROM tab1 AS cor0
----
1248
1404
570

query I rowsort
SELECT ALL + cor0.col0 FROM tab1, tab0 AS cor0
----
9 values hashing to 8b49799942a9e353a3d279cf64ef3f63

query I rowsort
SELECT ALL + cor0.col1 AS col0 FROM tab0, tab0 AS cor0
----
9 values hashing to 585a41a52c0c6c0d697b5d39265b74dc

query I rowsort
SELECT - 92 * - col0 FROM tab1 AS cor0
----
276
5888
7360

query I rowsort
SELECT distinct - col1 + col1 + col1 FROM tab0
----
86
91
97

query I rowsort
SELECT 79 AS col1 FROM tab0
----
79

query I rowsort
SELECT cor1.col2 AS col1 FROM tab2, tab2 AS cor0, tab2 AS cor1
----
27 values hashing to 40fd8cc0de92ea68d73634c2d8f75bf5

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col0 col2 FROM tab0 AS cor0
----
24
35
89

query I rowsort
SELECT - col1 * - col2 AS col0 FROM tab1
----
1248
1404
570

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT col1 + - col1 col2 FROM tab2
----
0
0
0

query I rowsort
SELECT distinct col2 + col0 * col0 AS col1 FROM tab2
----
6110
6279
76

query I rowsort
SELECT ALL + col1 + col1 AS col2 FROM tab2
----
118
34
62

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT distinct col2 + tab2.col0 col0 FROM tab2
----
104
117
34

query I rowsort
SELECT ALL + col0 * col1 FROM tab1
----
1040
640
78

skipif postgresql # PostgreSQL requires AS when renaming output columns
query I rowsort
SELECT ALL + col1 col2 FROM tab2
----
17
31
59

query I rowsort
SELECT col1 * col2 AS col2 FROM tab2
----
1534
646
837

