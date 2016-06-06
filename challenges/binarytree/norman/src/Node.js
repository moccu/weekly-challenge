module.exports = Node;


function Node(key, value, parent) {
	this.parent = parent;
	this.left = null;
	this.right = null;

	this.insert(key, value);
}

Node.prototype.insert = function(key, value) {
	if (this.key) {
		if (key < this.key) {
			return this.left
				? this.left.insert(key, value)
				: (this.left = new Node(key, value, this));
		} else if (key > this.key) {
			return this.right
				? this.right.insert(key, value)
				: (this.right = new Node(key, value, this));
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