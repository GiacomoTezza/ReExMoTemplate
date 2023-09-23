db.createUser(
    {
        user: "user",
        pwd: "#[mongo-password]",
        roles: [
            {
                role: "readWrite",
                db: "#[projectname]"
            }
        ]
    }
);