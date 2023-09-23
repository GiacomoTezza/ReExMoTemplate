const User = require("../db/user").User;
const users = require("./testDataDump/users.json");

const options = { maxTimeMS: 30000 };

async function deleteAll() {
  await User.deleteMany({}, options);
}

async function populateAll() {
  await User.create(users);
}

async function manualPopulate() {
  await deleteAll()
    .then(() => console.log("Database erased"))
    .catch((err) => console.log(err));
  await populateAll()
    .then(() => console.log("Database populated"))
    .catch((err) => console.log(err));
}

if (require.main === module) {
  manualPopulate();
}

exports.manualPopulate = manualPopulate;
exports.deleteAll = deleteAll;
exports.populateAll = populateAll;