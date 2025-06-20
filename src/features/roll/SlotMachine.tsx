import { Box, Text, useColorModeValue } from '@chakra-ui/react';
import { motion, useAnimate } from 'framer-motion';
import { useEffect, useMemo, useRef } from 'react';

interface SlotMachineProps {
  options: string[];
  isSpinning: boolean;
  onComplete: (result: string) => void;
}

const ITEM_HEIGHT = 80; // Height of each option item in pixels

const SlotMachine = ({ options, isSpinning, onComplete }: SlotMachineProps) => {
  const [scope, animate] = useAnimate();
  const bgColor = useColorModeValue('gray.200', 'gray.700');
  const highlightColor = useColorModeValue('brand.500', 'brand.300');

  const animationList = useMemo(() => {
      if (options.length === 0) return [];
      const repeats = Math.max(5, Math.ceil(50 / options.length));
      return Array(repeats).fill(options).flat();
  }, [options]);

  const onCompleteRef = useRef(onComplete);
  onCompleteRef.current = onComplete;

  useEffect(() => {
    const startAnimation = async () => {
      if (isSpinning && scope.current && options.length > 0) {
        const newResultIndex = Math.floor(Math.random() * options.length);
        
        const totalRepeats = Math.max(5, Math.ceil(50 / options.length));
        const targetRepeatIndex = totalRepeats - 2; 
        const targetY = -((targetRepeatIndex * options.length) + newResultIndex) * ITEM_HEIGHT;

        await animate(scope.current, { y: 0 }, { duration: 0 });

        await animate(
          scope.current,
          { y: targetY },
          {
            duration: 3,
            ease: 'circOut',
          }
        );
        onCompleteRef.current(options[newResultIndex]);
      }
    };
    startAnimation();
  }, [isSpinning]);

  return (
    <Box
      w={{ base: '90%', md: '500px' }}
      h={`${ITEM_HEIGHT}px`}
      bg={bgColor}
      borderRadius="lg"
      overflow="hidden"
      position="relative"
      boxShadow="inner"
      _after={{
        content: '""',
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        zIndex: 3,
        bgGradient: `linear(to-b, ${bgColor}, transparent 30%, transparent 70%, ${bgColor})`,
        pointerEvents: 'none',
      }}
    >
      <Box 
        position="absolute"
        top="0"
        left="0"
        right="0"
        h="100%"
        zIndex={2}
        borderY="2px solid"
        borderColor={highlightColor}
        pointerEvents="none"
      />
      <motion.div ref={scope}>
        {animationList.map((option, i) => (
          <Text
            key={`${option}-${i}`}
            h={`${ITEM_HEIGHT}px`}
            lineHeight={`${ITEM_HEIGHT}px`}
            textAlign="center"
            fontSize="4xl"
            fontWeight="bold"
            isTruncated
            px={4}
          >
            {option}
          </Text>
        ))}
      </motion.div>
    </Box>
  );
};

export default SlotMachine;