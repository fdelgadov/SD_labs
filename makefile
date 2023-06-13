c:
	javac $D/*.java
	jar -cf $F.jar $D/*.class
	del $D\*.class