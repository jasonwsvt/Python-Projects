import webbrowser

f = open("index.html", "w")
f.write("""<html>
	<body>
		<h1>
	Stay tuned for our amazing summer sale!
		</h1>
	</body>
</html>""")
f.close()

webbrowser.open("index.html", 2, True)