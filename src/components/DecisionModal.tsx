import { Modal, ModalOverlay, ModalContent, ModalHeader, ModalCloseButton, ModalBody } from "@chakra-ui/react"
import CoinToss from "./CoinToss";
import YesNoResult from "./YesNoResult";

interface DecisionModalProps {
    type: 'yesno' | 'coin' | null;
    title: string;
    isOpen: boolean;
    onClose: () => void;
}

const DecisionModal = ({ type, title, isOpen, onClose }: DecisionModalProps) => {
    const modalBodyMinHeight = "280px";

    return (
        <Modal isOpen={isOpen} onClose={onClose} isCentered size="md" motionPreset="slideInBottom">
            <ModalOverlay bg='blackAlpha.600' backdropFilter='blur(5px)' />
            <ModalContent mx={4} borderRadius="xl">
                <ModalHeader textAlign="center">{title}</ModalHeader>
                <ModalCloseButton />
                <ModalBody minH={modalBodyMinHeight} display="flex" alignItems="center" justifyContent="center">
                    {type === 'yesno' && <YesNoResult key={isOpen ? 'yesno-open' : 'yesno-closed'} />}
                    {type === 'coin' && <CoinToss key={isOpen ? 'coin-open' : 'coin-closed'} />}
                </ModalBody>
            </ModalContent>
        </Modal>
    );
};

export default DecisionModal;