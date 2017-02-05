import tensorflow as tf

x_data = [1, 2, 3, 4]
y_data = [1, 2, 3, 4]

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

hyphothesis = W * X + b

cost = tf.reduce_mean(tf.square(hyphothesis - Y))

a = tf.Variable(0.11)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(101):
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    if step % 20 == 0:
        print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W), sess.run(b))

print(sess.run(hyphothesis, feed_dict={X:7}))
print(sess.run(hyphothesis, feed_dict={X:15}))
