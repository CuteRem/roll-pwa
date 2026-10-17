import { extendTheme, type ThemeConfig } from '@chakra-ui/react';
import { mode } from '@chakra-ui/theme-tools';

const config: ThemeConfig = {
  initialColorMode: 'light',
  useSystemColorMode: false,
};

const theme = extendTheme({
  config,
  colors: {
    brand: {
      50: '#EBF8FF',
      100: '#C3DAFE',
      200: '#A3BFFA',
      300: '#7F9CF5',
      400: '#667EEA',
      500: '#5A67D8',
      600: '#4C51BF',
      700: '#434190',
      800: '#3C366B',
      900: '#322F5A',
    },
  },
  styles: {
    global: (props: any) => ({
      'body': {
        bg: 'gray.50',
        color: 'gray.800',
        lineHeight: 'base',
      },
    }),
  },
});

export default theme;
