TESTS = {
	"AND" : [[
		"basic",
		"TTF\n",
"""A + B => X
C + X => Y
D + A => Z
=ABC
?XYZ"""
	],[
		"nested",
		"TTTFFF\n",
"""A+(B+C+(D+E+(F+G)+H))+I=>Z
((((A)+B)+C)+D)+(E+(F+(G)))=>Y
A+B+(Z+Y)+C+D+(E+(F+G))=>X
A+(B+C+(M+E+(F+G)+H))+I=>W
((((A)+B)+M)+D)+(O+(F+(G)))=>V
((((A)+B)+W)+D)+(V+(F+(G)))=>U
=ABCDEFGHI
?ZYXWVU
"""
	],[
		"fake ?",
		"FF??F\n",
"""A+B+C+X=>Z
A+Z=>X
A+U=>V
A+V=>U
A+B=>J
M+N=>J
=AB
?ZXVUJ
"""
]],

	"OR " : [[
		"basic",
		"TTF\n",
"""A | B => X
A | D => Y
D | E => Z
=ABC
?XYZ
"""
	],[
		"nested",
		"TFT\n",
"""Q|(W|E)|R=>P
(A+S)|(S+D)=>L
(Z)|(X|C|(V|B|X)|V)|N=>M
=WSN
?PLM
"""
]],

	"XOR" : [[
		"basic",
		"TTFF\n",
"""A ^ D => Z
D ^ B => Y
A ^ A => X
D ^ D => W
=AB
?ZYXW
"""
	],[
		"nested",
		"TTF\n",
"""Q^(W^Q^(E^E))=>P
A^S^D^F^G^H^J^K=>L
(Z^X)^(C^V)=>M
=EWKCV
?PLM
"""
]],

	"NOT" : [[
		"basic",
		"FT\n",
"""!A => Z
!B => X
=A
?ZX
"""
	],[
		"nested",
		"TTF\n",
"""!(!(Q))+(!(!(!(W))))=>P
!(A|S+!(D^!F))=>L
!(Z)|!(((X)))=>M
=QDFZX
?PLM
"""
	],[
	"incoherent",
	"FF\n",
"""Q=>P
W=>P
!(A)=>L
A=>L
=QA
?PL"""
]],

	"PAR" : [[
		"basic",
		"TF\n",
"""A+(B|C)=>Z
D+(E^F)=>Y
=ACEF
?ZY
"""
]],

	"=>+" :[[
		"basic",
		"FTF\n",
"""Q+W+A+S=>P+L
Z+X=>P+M
=QWASZ
?PLM
"""
	],[
		"harder",
		"TTT\n",
"""Q+W=>P+L+M
A+S=>P+L+M
!(Z+X)=>P+L+M
=QWAS
?PLM
"""
]],
	"INC" :[[
		"basic",
		"TTTT\n",
"""B=>C
E=>F
D=>E
F=>G
G=>H
C=>D
A=>B
=A
?EFGH
"""
	],[
		"deeper",
		"TTTTTTTTTTTTTTTTTTTTTTTTTT\n",
"""Z=>Y
Y=>X
X=>W
W=>V
V=>U
U=>T
T=>S
S=>R
R=>Q
Q=>P
P=>O
O=>N
N=>M
M=>L
L=>K
K=>J
J=>I
I=>H
H=>G
G=>F
F=>E
E=>D
D=>C
C=>B
B=>A
A=>Z
=A
?ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""
	],[
		"mixed",
		"TFTFTFTFTFTFTFTFTFTFTFTFTF\n",
"""!(Y)=>X
!(C)=>B
!(J)=>I
!(P)=>O
!(U)=>T
!(X)=>W
!(T)=>S
!(W)=>V
!(R)=>Q
!(Z)=>Y
!(N)=>M
!(S)=>R
!(K)=>J
!(M)=>L
!(O)=>N
!(H)=>G
!(E)=>D
!(Q)=>P
!(L)=>K
!(V)=>U
!(D)=>C
!(I)=>H
!(G)=>F
!(A)=>Z
!(F)=>E
!(B)=>A
=A
?ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""
	]],
		"MIX":
		[[
			"basic",
			"TTT\n",
"""P^(!(A|S)+D|(!(F)+G))=>L
!(Q)^(W+!(E|R)^!(T+Y))|U|(I+O)=>P
!(L^P)^(Z+(X+(C+(V+(B+N)))))=>M
=QWRYIADFGZXCVB
?PLM
"""
	]]
}

#TESTS["NOTHING"] =
[[
	"basic",
	"TTTFFF\n",
	"""=ABCDEF\n?ABCXYZ"""
],[
	"Illegal: input A++B",
	"ES ERROR : Illegal instruction.\n",
	"""A++B=>\n"""
],[
	"Illegal: input (",
	"ES ERROR : Illegal instruction.\n",
	"""A+(=>B\n"""
],[
	"Illegal: input )",
	"ES ERROR : Illegal instruction.\n",
	"""A+)=>B\n"""
],[
	"Illegal: input X =>\\n",
	"ES ERROR : Illegal instruction.\n",
	"""A + B =>\n"""
],[
	"Illegal: input \\n=> X",
	"ES ERROR : Illegal instruction.\n",
	"""=> X\n"""
],[
	"Illegal: input AA=> B",
	"ES ERROR : Illegal instruction.\n",
	"""AA=>B\n"""
],[
	"Illegal: input ?=>",
	"ES ERROR : Illegal instruction.\n",
	"""?A=>A\n"""
],[
	"Illegal: input =>=",
	"ES ERROR : Illegal instruction.\n",
	"""=AB + D => C\n"""
],[
	"Illegal: input =?",
	"ES ERROR : Illegal instruction.\n",
	"""=AB?CD\n"""
],[
	"Illegal: useless line",
	"ES ERROR : Illegal instruction.\n",
	"""A+D\n"""
]]

