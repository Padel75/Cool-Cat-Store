<template>
  <pre>{{ asciiTable }}</pre>
</template>

<script>
import { getInvoices } from '@/api/payment';

export default {
  name: 'Invoice',
  data() {
    return {
      invoice: [],
      asciiTable: ''
    };
  },
  methods: {

    longestEntry(key) {
      let maxLength = 0;
      const invoice = this.invoice
      for (const product of invoice.products) {
        let entry;
        let title;
        switch (key) {
          case 'id':
            entry = invoice.id.toString();
            title = 'ID'
            break;
          case 'date':
            entry = invoice.date.slice(0, -13);
            title = 'DATE'
            break;
          case 'name':
            entry = product.name;
            title = 'PRODUCT'
            break;
          case 'price':
            entry = product.price.toFixed(2);
            title = 'PRICE'
            break;
          case 'quantity':
            entry = product.quantity.toString();
            title = 'QTY'
            break;
          case 'total_cost':
            entry = invoice.total_cost.toFixed(2);
            title = 'TOTAL COST'
            break;
          default:
            return 0;
        }
        if (entry.length > maxLength) {
          maxLength = entry.length;
          if (maxLength < title.length) {
            maxLength = title.length;
          }
        }
      }
      return maxLength;
    },
    createAsciiTable(invoice) {
      const lstr_id = this.longestEntry('id')
      const lstr_date = this.longestEntry('date')
      const lstr_name = this.longestEntry('name')
      const lstr_price = this.longestEntry('price')
      const lstr_qty = this.longestEntry('quantity')
      const lstr_tcost = this.longestEntry('total_cost')

      const c_id    = ' '.repeat(Math.ceil(lstr_id/2))+("ID")+' '.repeat(Math.floor(lstr_id/2))
      const c_date  = ' '.repeat(Math.ceil(lstr_date/2)-1)+("DATE")+' '.repeat(Math.floor(lstr_date/2)-1)
      const c_name  = ' '.repeat(Math.ceil(lstr_name/2)-3)+("PRODUCT")+' '.repeat(Math.floor(lstr_name/2)-2)
      const c_price = ' '.repeat(Math.ceil(lstr_price/2)-2)+("PRICE")+' '.repeat(Math.floor(lstr_price/2)-1)
      const c_qty   = ' '.repeat(Math.ceil(lstr_qty/2)-1)+("QTY")+' '.repeat(Math.floor(lstr_qty/2))
      const c_tcost = ' '.repeat(Math.ceil(lstr_tcost/2)-4)+("TOTAL COST")+' '.repeat(Math.floor(lstr_tcost/2)-4)

      let table = `+${'-'.repeat(c_id.length)}+${'-'.repeat(c_date.length)}+${'-'.repeat(c_name.length)}+${'-'.repeat(c_price.length)}+${'-'.repeat(c_qty.length)}+${'-'.repeat(c_tcost.length)}+\n`;
      table +=    `|${c_id}|${c_date}|${c_name}|${c_price}|${c_qty}|${c_tcost}|\n`;
      table +=    `+${'-'.repeat(c_id.length)}+${'-'.repeat(c_date.length)}+${'-'.repeat(c_name.length)}+${'-'.repeat(c_price.length)}+${'-'.repeat(c_qty.length)}+${'-'.repeat(c_tcost.length)}+\n`;


      for (const [index, product] of invoice.products.entries()) {
        let id='';
        let date='';
        let totalCost='';
        if(index == 0){
          id = invoice.id.toString()
        }
        if(index == 0){
          date = invoice.date.slice(0, -13)
        }
        if(index == invoice.products.length-1){
          totalCost = invoice.total_cost.toFixed(2)
        }
        table += `| ${id.padEnd(lstr_id)} | ${date.padEnd(lstr_date)} | ${product.name.padEnd(lstr_name)} | ${product.price.toFixed(2).padEnd(lstr_price)} | ${product.quantity.toString().padEnd(lstr_qty)} | ${totalCost.padEnd(lstr_tcost)} |\n`;
      }
      table +=`+${'-'.repeat(c_id.length)}+${'-'.repeat(c_date.length)}+${'-'.repeat(c_name.length)}+${'-'.repeat(c_price.length)}+${'-'.repeat(c_qty.length)}+${'-'.repeat(c_tcost.length)}+\n`;
      return table;
    }
  },
  mounted() {
    getInvoices().then(response => {
      this.invoice = response.data.invoices.at(-1);
      this.asciiTable = this.createAsciiTable(this.invoice);
    });
  }
};
</script>

<style scoped>

</style>
