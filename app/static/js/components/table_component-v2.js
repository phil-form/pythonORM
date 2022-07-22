export class TableComponentV2 {
    constructor(tableConfig) {
        this.table = document.createElement('table');
        this.tableCaption = document.createElement('caption');
        this.tableHead = document.createElement('thead');
        this.tableBody = document.createElement('tbody');

        this.initTable(tableConfig);
    }

    initTable(tableConfig) {

        if (tableConfig.classList && tableConfig.classList.length != 0) {
            const tableClasslist = this.table.classList;
            tableConfig.classList.array.forEach(c => {
                tableClasslist.add(c);
            });
        }

        if (tableConfig.caption && tableConfig.caption != '') {
            this.tableCaption.innerText = tableConfig.caption;
            this.table.appendChild(this.tableCaption);
        }

        if (tableConfig.columns && tableConfig.columns.length != 0) {
            const tableHead_tr = document.createElement('tr');

        }
    }
}

conf = {
    data: data,
    caption: "List of items",
    classList: [
        'table',
        'table-stripped',
        'table-hover'
    ],
    columns: [
        {name: 'ID', value: 'userid'},
        {name: 'Name', value: 'username'},
        {name: 'Email', value: 'useremail'},
        {name: 'Descritpion', value: 'userdescritpion'},
        {name: 'test', value: 'usertest', input: 'text'},
        {name: 'Roles', value: () => {}},
    ],
    actions: [
        {name: 'update', type: 'button', classList: ['btn btn-primary'], cb: () => {}, event: 'click', displayType: 'row'},
        {name: 'remove', type: 'button', classList: ['btn btn-primary'], cb: () => {}, event: 'click', displayType: 'row'},
        {name: 'test', type: 'a', classList: ['btn btn-primary'], cb: "href", displayType: 'row'}
    ]
}

