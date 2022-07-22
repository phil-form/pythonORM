export let ajaxConfig = {
    headers: []
};

export function sendAjax(url, method='get', data = null)
{
    return new Promise((resolve, reject) =>
    {
        const request =  new XMLHttpRequest();

        request.addEventListener('readystatechange', (e) =>
        {
            if(request.readyState === 4)
            {
                const data = request.responseText

                if(/^2[0-9]{2}$/.test(request.status))
                {
                    resolve(data);
                } else
                {
                    reject(data);
                }
            }
        });

        request.open(method, url, true);

        if(ajaxConfig.headers.length > 0)
        {
            for(let header of ajaxConfig.headers)
            {
<<<<<<< HEAD
                const methods = ajaxConfig.headers.methods;
=======
                const methods = header.methods;
>>>>>>> 11ade11afa9f83ba721f142f68f06316dcb913f5
                if(methods.includes(method) || methods.includes('ALL'))
                {
                    request.setRequestHeader(header.key, header.value);
                }
            }
        }

        request.send(data);
    })
}