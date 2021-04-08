
window.addEventListener("load", function(){
    document.getElementById("descarga").addEventListener("click", function(){
        let workbook = XLSX.utils.book_new();
        let tables = document.getElementsByTagName("table");
        for(let i = 0; i < tables.length; i++){
            let name = tables[i].caption.innerText
            let worksheet = XLSX.utils.table_to_sheet(tables[i]);
            XLSX.utils.book_append_sheet(workbook, worksheet, name);
        }
        let date = new Date().toISOString().slice(0, 10)
        XLSX.writeFile(workbook, 'Reporte' + date + '.xlsx');
    });
});