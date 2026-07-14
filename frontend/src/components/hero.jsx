import { motion } from "framer-motion";

function Hero() {
  return (
    <motion.div

      initial={{ opacity:0,y:40 }}

      animate={{ opacity:1,y:0 }}

      transition={{ duration:1 }}

      className="text-center py-16"

    >

      <h1 className="text-6xl font-bold text-white">

        Customer Churn Prediction

      </h1>

      <p className="mt-6 text-gray-300 text-xl">

        Predict whether a customer will leave your company using Machine Learning.

      </p>

    </motion.div>
  );
}

export default Hero;