const AbstractUser = require('../users/AbstractUser');
const AnonymousUser = require('../users/AnonymousUser');
// const Admin = require('../users/Admin');
// const Editor = require('../users/Editor');
// const Reader = require('../users/Reader');

const userTypes = {
    'abstractUser': AbstractUser,
    'anonymousUser': AnonymousUser
    // 'admin': Admin,
    // 'user': User,
};

class UserType {
    constructor() {
        if (this.constructor === UserType) {
            throw new TypeError('UserType cannot be instantiated because it is an abstract class');
        }
    }

    static getUserType(userType) {
        return userTypes[userType];
    }
}

module.exports = UserType;