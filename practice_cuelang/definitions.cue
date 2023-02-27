// _#,#はは定義であることを示している。
// // ... はそれ定義にあるプロパティ以外は何も定義できないこと(closed)を示す。
// ...にすると定義以外のプロパティも宣言できる

#Conn: {
	address: string
	port: int
	protocol: string
	// ...
}

lossy: #Conn & {
	address: "1.2.3.4"
	port: 8888
	protocol: "udp"
	foo:2
	bar: 3
}
