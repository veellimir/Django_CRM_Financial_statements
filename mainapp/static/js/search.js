new MultiSelectTag('counterparty', {
    rounded: true,
    shadow: true,
    placeholder: 'Найти',
    tagColor: {
        textColor: '#327b2c',
        borderColor: '#92e681',
        bgColor: '#eaffe6',
    },
    onChange: function(values) {
        console.log(values)
    }
})
