#include<stdio.h>
#include <stdlib.h>

// Definition for a binary tree node.
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
};


int rangeSumBST(struct TreeNode* root, int low, int high) {
	return rangeSumBSTHelper(root, low, high, 0);
}

int rangeSumBSTHelper(struct TreeNode* root, int low, int high, int sum) {
	if (root == NULL) {
		return 0;
	}

	if (root->val < low) {
		return rangeSumBSTHelper(root->right, low, high, sum);
	}

	if (root->val > high) {
		return rangeSumBSTHelper(root->left, low, high, sum);
	}

	return root->val + rangeSumBSTHelper(root->right, low, high, sum) + rangeSumBSTHelper(root->left, low, high, sum);
}