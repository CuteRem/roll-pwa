import { useState } from 'react';
import { Button, Heading, VStack, IconButton, useColorModeValue } from '@chakra-ui/react';
import { FaArrowLeft } from 'react-icons/fa';
import { Wheel } from '../../types';
import SlotMachine from './SlotMachine';

interface RollScreenProps {
  wheel: Wheel;
  onBack: () => void;
}

const RollScreen = ({ wheel, onBack }: RollScreenProps) => {
  const [isSpinning, setIsSpinning] = useState(false);
  const [result, setResult] = useState<string | null>(null);
  const bgColor = useColorModeValue('gray.100', 'gray.800');

  const getOptions = () => {
    if (wheel.type === 'number') {
      const options = [];
      const min = wheel.min ?? 1;
      const max = wheel.max ?? 100;
      for (let i = min; i <= max; i++) {
        options.push({ text: i.toString() });
      }
      return options;
    }
    return wheel.options;
  };
  
  const options = getOptions();

  const handleSpin = () => {
    if (isSpinning) return;
    setResult(null); // Reset result before spinning
    setIsSpinning(true);
  };

  const handleSpinComplete = (finalResult: string) => {
    setResult(finalResult);
    setIsSpinning(false);
  };

  return (
    <VStack minH="100vh" p={4} spacing={8} justify="center" overflowX="hidden" bg={bgColor}>
        <IconButton 
            aria-label="Back" 
            icon={<FaArrowLeft />} 
            onClick={onBack} 
            isRound 
            position="absolute" top={6} left={6}
            size="lg"
            variant="ghost"
        />

        <Heading as="h1" size="2xl" textAlign="center" px={{base: 4, md: 16}}>
          {wheel.title}
        </Heading>
        
        <SlotMachine
            options={options.map(o => o.text)}
            isSpinning={isSpinning}
            onComplete={handleSpinComplete}
        />

        <Button
          colorScheme="brand"
          size="lg"
          onClick={handleSpin}
          isLoading={isSpinning}
          loadingText="滚动中..."
          px={16}
          py={8}
          fontSize="2xl"
          boxShadow="lg"
          rounded="full"
          isDisabled={isSpinning}
        >
          {result ? "再来一次" : "开始滚动"}
        </Button>
    </VStack>
  );
};

export default RollScreen;