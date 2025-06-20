import { Box, Flex, Heading, Spacer, useColorMode, IconButton, useColorModeValue } from '@chakra-ui/react';
import { FaSun, FaMoon } from 'react-icons/fa';

const Header = () => {
  const { colorMode, toggleColorMode } = useColorMode();
  const bg = useColorModeValue('rgba(255, 255, 255, 0.8)', 'rgba(23, 25, 35, 0.8)');

  return (
    <Box
      as="header"
      bg={bg}
      py={3}
      px={{ base: 4, md: 8 }}
      boxShadow="sm"
      position="sticky"
      top={0}
      zIndex="sticky"
      backdropFilter="saturate(180%) blur(5px)"
    >
      <Flex align="center" maxW="container.lg" mx="auto">
        <Heading as="h1" size="lg" letterSpacing="tight">
          肉店大师
        </Heading>
        <Spacer />
        <IconButton
          aria-label="Toggle theme"
          icon={colorMode === 'dark' ? <FaSun /> : <FaMoon />}
          onClick={toggleColorMode}
          isRound
          variant="ghost"
        />
      </Flex>
    </Box>
  );
};

export default Header;