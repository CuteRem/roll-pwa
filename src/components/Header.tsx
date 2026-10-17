import { Box, Flex, Heading, Spacer } from '@chakra-ui/react';

const Header = () => {
  const bg = 'rgba(255, 255, 255, 0.8)';

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
      </Flex>
    </Box>
  );
};

export default Header;
