function Node(key, value) {
	this.left = null;
	this.right = null;

	this.insert(key, value);
}

Node.prototype.insert = function(key, value) {
	if (this.key) {
		if (key < this.key) {
			return this.left
				? this.left.insert(key, value)
				: (this.left = new Node(key, value));
		} else if (key > this.key) {
			return this.right
				? this.right.insert(key, value)
				: (this.right = new Node(key, value));
		} else {
			return null;
		}
	} else {
		this.key = key;
		this.value = value;
		return this;
	}
};

Node.prototype.find = function(key) {
	if (key === this.key) {
		return this.value;
	} else if (key < this.key) {
		return this.left ? this.left.find(key) : undefined;
	} else {
		return this.right ? this.right.find(key) : undefined;
	}
};

Node.prototype.toObject = function() {
	return {
		key: this.key,
		value: this.value,
		left: this.left ? this.left.toObject() : null,
		right: this.right ? this.right.toObject() : null
	};
};

function Tree() {
	this.root = null;
}

Tree.prototype.insert = function(key, value) {
	if (this.root) {
		return this.root.insert(key, value);
	} else {
		return (this.root = new Node(key, value));
	}
};

Tree.prototype.find = function(key) {
	return this.root ? this.root.find(key) : undefined;
};

Tree.prototype.parse = function(str) {
	this.root = (function(data, parent) {
		if (!data) {
			return null;
		}

		var node = new Node(parseInt(data.key, 10), data.value);
		node.left = arguments.callee(data.left, node);
		node.right = arguments.callee(data.right, node);

		return node;
	})(JSON.parse(str), null);
};

Tree.prototype.stringify = function() {
	var data = this.root ? this.root.toObject() : {};
	return JSON.stringify(data);
};

module.exports = Tree;
