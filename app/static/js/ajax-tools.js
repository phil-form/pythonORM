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
                const methods = header.methods;
                if(methods.includes(method) || methods.includes('ALL'))
                {
                    request.setRequestHeader(header.key, header.value);
                }
            }
        }

        request.send(data);
    })
}