print('Start creating database ##########################')
db = db.getSiblingDB('jotunheim');
db.createUser(
    {
        user: 'root',
        pwd:  'pass12345',
        roles: [{role: 'readWrite', db: 'jotunheim'}],
    }
);

db = db.getSiblingDB('jotunheim_test');
db.createUser(
    {
        user: 'root',
        pwd:  'pass12345',
        roles: [{role: 'readWrite', db: 'jotunheim_test'}],
    }
);
print('End creating database ##########################')
