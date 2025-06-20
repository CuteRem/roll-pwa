import { Box, Container, VStack } from '@chakra-ui/react';
import Header from '../../components/Header';
import QuickRoll from './QuickRoll';
import { Wheel } from '../../types';

interface DashboardProps {
    onStartWheel: (wheel: Wheel) => void;
}

const Dashboard = ({ onStartWheel }: DashboardProps) => {
    return (
        <Box>
            <Header />
            <Container maxW="container.lg" py={{base: 6, md: 10}}>
                <VStack spacing={8} align="stretch">
                    <QuickRoll onStartWheel={onStartWheel} />
                </VStack>
            </Container>
        </Box>
    );
};

export default Dashboard;