export class TableComponent
{
    constructor(tableConfig) {
        this.html = document.createElement('table');
        this.initTable(tableConfig)
    }

    initTable(tableConfig)
    {
        this.html.classList.add('table');
        this.html.classList.add('table-striped');
        this.html.classList.add('table-hover');
        this.thead = document.createElement('thead');
        this.tbody = document.createElement('tbody');
        
        let first = true;
        let thead_tr = document.createElement('tr');

        for(const row of tableConfig.data)
        {
            let tr = document.createElement('tr')
            for (const col of tableConfig.columns)
            {
                if (first)
                {
                    const th = document.createElement('th')
                    th.scope = 'col';
                    th.innerText = col.columName;
                    thead_tr.appendChild(th);
                }
                if (col.value)
                {
                    const value = 
                }
                if (col.valueCb)
                {

                }
            }
        }

    }

    processRow(row, value)
    {
        if (value.indexOf('.') !== -1)
        {
            let objMemberName = value.split('.');
            for (const val of objMemberName)
            {
                row = this.processRow(row, val);
            }
            return row;
        }
        return row[value];
    }
}

{
    data: [{}, {}];
    columns: [
        { columName: '', value: '', valueCb: '', type: ''}
    ]
}