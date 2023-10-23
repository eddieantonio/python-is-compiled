# Convert test_2 to Windows 1252, just to upset the decoder.
test_1.py: test_2.py
	iconv -f utf8 -t cp1252
