from faker import Faker
from faker.providers import DynamicProvider

class StudentsGenerator():
     def generate_students(self):
          student_deparment_provider = DynamicProvider(
               provider_name="student_deparment",
               elements=[
                    "Department of Logistics and Maritime Studies", 
                    "Department of Management and Marketing",
                    "School of Accounting and Finance",
                    "Department of Applied Mathematics",
                    "Department of Computing",
                    "Department of Data Science and Artificial Intelligence",
                    "Department of Building Environment and Energy Engineering",
                    "Department of Building and Real Estate",
                    "Department of Civil and Environmental Engineering",
                    "Department of Land Surveying and Geo-Informatics"
               ],
          )



          fake = Faker()

          # then add new provider to faker instance
          fake.add_provider(student_deparment_provider)

          # now you can use:
          print(fake.student_deparment())
