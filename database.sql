BEGIN TRANSACTION;CREATE TABLE "RecHasTag" (
	"ID"	INTEGER,
	"ID_Rec"	TEXT NOT NULL,
	"Name"	TEXT NOT NULL,
	FOREIGN KEY("Name") REFERENCES "Tags"("Name"),
	FOREIGN KEY("ID_Rec") REFERENCES "Recipies"("ID_Rec"),
	PRIMARY KEY("ID" AUTOINCREMENT)
);INSERT INTO "RecHasTag" VALUES(1,'00001','Schwein');INSERT INTO "RecHasTag" VALUES(2,'00001','Schweinebauch');INSERT INTO "RecHasTag" VALUES(3,'00001','Braten');INSERT INTO "RecHasTag" VALUES(4,'00001','Gordon Ramsay');INSERT INTO "RecHasTag" VALUES(5,'00002','Steak');INSERT INTO "RecHasTag" VALUES(6,'00002','Rind');INSERT INTO "RecHasTag" VALUES(7,'00002','Tacos');INSERT INTO "RecHasTag" VALUES(8,'00002','Gordon Ramsay');INSERT INTO "RecHasTag" VALUES(9,'00002','Fastfood');INSERT INTO "RecHasTag" VALUES(10,'00002','Einfach');CREATE TABLE "Recipies" (
	"ID_Rec"	TEXT NOT NULL,
	"Name"	TEXT NOT NULL,
	PRIMARY KEY("ID_Rec")
);INSERT INTO "Recipies" VALUES('00001','SLOW-ROASTED PORK BELLY WITH FENNEL');INSERT INTO "Recipies" VALUES('00002','BEEF TACOS WITH WASABI MAYO');CREATE TABLE "Tags" (
	"Name"	TEXT NOT NULL,
	PRIMARY KEY("Name")
);INSERT INTO "Tags" VALUES('Schweinebauch');INSERT INTO "Tags" VALUES('Braten');INSERT INTO "Tags" VALUES('Gordon Ramsay');INSERT INTO "Tags" VALUES('Schwein');INSERT INTO "Tags" VALUES('Steak');INSERT INTO "Tags" VALUES('Fastfood');INSERT INTO "Tags" VALUES('Rind');INSERT INTO "Tags" VALUES('Einfach');INSERT INTO "Tags" VALUES('Tacos');DELETE FROM "sqlite_sequence";INSERT INTO "sqlite_sequence" VALUES('RecHasTag',10);COMMIT;