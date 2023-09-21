resource "aws_s3_bucket_acl" "bucket_sagemaker" {
  bucket = aws_s3_bucket.bucket_sagemaker.id
  acl    = "private"
  depends_on = [aws_s3_bucket_ownership_controls.s3_bucket_acl_ownership]
}

# Resource to avoid error "AccessControlListNotSupported: The bucket does not allow ACLs"
resource "aws_s3_bucket_ownership_controls" "s3_bucket_acl_ownership" {
  bucket = aws_s3_bucket.bucket_sagemaker.id
  rule {
    object_ownership = "ObjectWriter"
  }
}

resource "aws_s3_bucket" "bucket_sagemaker" {
  bucket = var.bucket_name
}
