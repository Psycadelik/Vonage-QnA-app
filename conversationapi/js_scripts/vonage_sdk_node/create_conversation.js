const Nexmo = require('nexmo')
require('dotenv').config()

const nexmo = new Nexmo({
    apiKey: process.env.NEXMO_API_KEY,
    apiSecret: process.env.NEXMO_API_SECRET,
    applicationId: process.env.NEXMO_APPLICATION_ID,
    privateKey: process.env.NEXMO_APPLICATION_PRIVATE_KEY_PATH
})

const aclPaths = {
    "paths": {
        "/*/users/**": {},
        "/*/conversations/**": {},
        "/*/sessions/**": {},
        "/*/devices/**": {},
        "/*/image/**": {},
        "/*/media/**": {},
        "/*/applications/**": {},
        "/*/push/**": {},
        "/*/knocking/**": {}
    }
}

Nexmo.generateJwt(process.env.NEXMO_APPLICATION_PRIVATE_KEY_PATH, {
    application_id: process.env.NEXMO_APPLICATION_ID,
    sub: "adrian",
    //expire in 24 hours
    exp: Math.round(new Date().getTime() / 1000) + 86400,
    acl: aclPaths
})

nexmo.conversations.create({
    "name": process.env.CONV_NAME,
    "display_name": process.env.CONV_DISPLAY_NAME
}, (error, result) => {
    if (error) {
        console.error(error);
    } else {
        console.log(result);
    }
});