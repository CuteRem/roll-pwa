import {
  Box,
  Button,
  Slide,
  useDisclosure,
  useColorModeValue,
  Text,
  HStack,
} from '@chakra-ui/react';
import { useRegisterSW } from 'virtual:pwa-register/react';

function PWAReloadPrompt() {
  const {
    needRefresh: [needRefresh],
    updateServiceWorker,
  } = useRegisterSW({
    onRegistered(r) {
      console.log(`SW Registered: ${r}`);
    },
    onRegisterError(error) {
      console.log('SW registration error', error);
    },
  });

  const { isOpen, onClose } = useDisclosure({ defaultIsOpen: needRefresh });

  const bg = useColorModeValue('white', 'gray.700');
  const textColor = useColorModeValue('gray.800', 'white');

  if (!isOpen) {
      return null;
  }

  return (
    <Box position="fixed" bottom="0" left="0" right="0" p={4} zIndex="overlay">
        <Slide direction="bottom" in={isOpen} style={{ zIndex: 10 }}>
        <Box
            p="4"
            color={textColor}
            bg={bg}
            shadow="lg"
            textAlign="center"
            borderRadius="md"
        >
            <HStack justify="center" spacing={4}>
            <Text>有新版本可用！</Text>
            <Button
                colorScheme="brand"
                onClick={() => updateServiceWorker(true)}
            >
                刷新
            </Button>
            <Button variant="ghost" onClick={onClose}>
                关闭
            </Button>
            </HStack>
        </Box>
        </Slide>
    </Box>
  );
}

export default PWAReloadPrompt;