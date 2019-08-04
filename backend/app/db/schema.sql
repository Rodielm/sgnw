CREATE TABLE "App" (
  "idApp" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "version" TEXT NOT NULL,
  "create_ts" TEXT NOT NULL
);

CREATE TABLE "Argument" (
  "idArgument" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "type" TEXT NOT NULL
);

CREATE TABLE "Group" (
  "idGroup" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "create_ts" TEXT NOT NULL
);

CREATE TABLE "Language" (
  "idLanguage" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL
);

CREATE TABLE "App_Language" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "app" INTEGER NOT NULL REFERENCES "App" ("idApp") ON DELETE CASCADE,
  "language" INTEGER NOT NULL REFERENCES "Language" ("idLanguage") ON DELETE CASCADE
);

CREATE INDEX "idx_app_language__app" ON "App_Language" ("app");

CREATE INDEX "idx_app_language__language" ON "App_Language" ("language");

CREATE TABLE "Notification" (
  "idNotification" INTEGER PRIMARY KEY AUTOINCREMENT,
  "summary" TEXT NOT NULL,
  "body" TEXT NOT NULL,
  "I10n_vers" TEXT NOT NULL,
  "create_ts" TEXT NOT NULL,
  "expire_ts" TEXT NOT NULL,
  "app" INTEGER NOT NULL REFERENCES "App" ("idApp")
);

CREATE INDEX "idx_notification__app" ON "Notification" ("app");

CREATE TABLE "Recipient" (
  "idRecipient" INTEGER PRIMARY KEY AUTOINCREMENT,
  "notification" INTEGER NOT NULL REFERENCES "Notification" ("idNotification") ON DELETE CASCADE
);

CREATE INDEX "idx_recipient__notification" ON "Recipient" ("notification");

CREATE TABLE "Role" (
  "idRol" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" TEXT NOT NULL
);

CREATE TABLE "Token" (
  "idToken" INTEGER PRIMARY KEY AUTOINCREMENT,
  "idUser" TEXT NOT NULL,
  "token" TEXT NOT NULL,
  "token_expires" DATETIME
);

CREATE TABLE "User" (
  "idUser" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" TEXT NOT NULL,
  "last_name" TEXT NOT NULL,
  "email" TEXT NOT NULL,
  "username" TEXT NOT NULL,
  "password" TEXT NOT NULL,
  "create_ts" TEXT NOT NULL
);

CREATE TABLE "UserGroup" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "group" INTEGER NOT NULL REFERENCES "Group" ("idGroup") ON DELETE CASCADE,
  "user" INTEGER NOT NULL REFERENCES "User" ("idUser") ON DELETE CASCADE,
  "recipient" INTEGER REFERENCES "Recipient" ("idRecipient") ON DELETE SET NULL
);

CREATE INDEX "idx_usergroup__group" ON "UserGroup" ("group");

CREATE INDEX "idx_usergroup__recipient" ON "UserGroup" ("recipient");

CREATE INDEX "idx_usergroup__user" ON "UserGroup" ("user");

CREATE TABLE "UserRecipient" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "recipient" INTEGER NOT NULL REFERENCES "Recipient" ("idRecipient") ON DELETE CASCADE,
  "user" INTEGER NOT NULL REFERENCES "User" ("idUser") ON DELETE CASCADE
);

CREATE INDEX "idx_userrecipient__recipient" ON "UserRecipient" ("recipient");

CREATE INDEX "idx_userrecipient__user" ON "UserRecipient" ("user");

CREATE TABLE "UserRole" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user" INTEGER NOT NULL REFERENCES "User" ("idUser") ON DELETE CASCADE,
  "role" INTEGER NOT NULL REFERENCES "Role" ("idRol") ON DELETE CASCADE,
  "recipient" INTEGER REFERENCES "Recipient" ("idRecipient") ON DELETE SET NULL
);

CREATE INDEX "idx_userrole__recipient" ON "UserRole" ("recipient");

CREATE INDEX "idx_userrole__role" ON "UserRole" ("role");

CREATE INDEX "idx_userrole__user" ON "UserRole" ("user")