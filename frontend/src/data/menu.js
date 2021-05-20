/*
 * Main and demo navigation arrays
 */

export default {
  'main': [
    {
      name: 'Home',
      to: '/backend/dashboard',
      icon: 'si si-speedometer'
    },
    {
      name: 'Products',
      heading: true
    },
    {
      name: 'Product List',
      icon: 'si si-energy',
      subActivePaths: '/backend/elements',
      sub: [
        {
          name: 'All',
          to: '/product/list'
        },
        {
          name: 'Outer',
          to: '/backend/blocks/options'
        },
        {
          name: 'Top',
          to: '/backend/blocks/forms'
        },
        {
          name: 'Bottom',
          to: '/backend/blocks/themed'
        }
      ]
    },
    {
      name: 'Register',
      icon: 'si si-badge',
      to: '/backend/elements',
    },
    {
      name: 'Edit',
      icon: 'si si-grid',
      to: '/backend/tables',
    },
    {
      name: 'Remove',
      icon: 'si si-note',
      to: '/backend/forms',
    },
  ]
}
