import tensorflow as tf
from tensorflow.python import pywrap_tensorflow

coref_op_library = tf.load_op_library("./coref_kernels.so")

spans = coref_op_library.spans
tf.NotDifferentiable("Spans")

regression = coref_op_library.regression
tf.NotDifferentiable("Regression")

memory = coref_op_library.memory
tf.NotDifferentiable("Memory")

tagging = coref_op_library.tagging
tf.NotDifferentiable("Tagging")

antecedents = coref_op_library.antecedents
tf.NotDifferentiable("Antecedents")

extract_mentions = coref_op_library.extract_mentions
tf.NotDifferentiable("ExtractMentions")

distance_bins = coref_op_library.distance_bins
tf.NotDifferentiable("DistanceBins")
